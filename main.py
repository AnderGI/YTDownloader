from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, UUID4, HttpUrl, StringConstraints 
from typing import Annotated
import subprocess
import uuid
import os
import threading
import time
from typing import Optional
from fastapi.responses import FileResponse
import mimetypes

def find_file_by_id(download_id):
    """
    Searches for a file in the download directory by ID, ignoring the extension.
    """
    for file in os.listdir(DOWNLOAD_DIR):
        if file.startswith(download_id):
            return os.path.join(DOWNLOAD_DIR, file)
    return None

app = FastAPI()

# Directory to store downloaded files
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# In-memory database for tracking downloads
downloads = {}



class TimeStampVideo(BaseModel):
    timestamp: Annotated[
        str, StringConstraints(pattern=r"^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$")
    ]


class YTVideoDownloadRequest(BaseModel):
    url: HttpUrl
    start_timestampt: TimeStampVideo
    end_timestampt: TimeStampVideo


class DownloadRequest(BaseModel):
    url: str
    start: Optional[str] = "0:00:00"
    end_or_length: Optional[str] = None
    type: Optional[str] = "video_start_end"

class DownloadStatus(BaseModel):
    id: str
    status: str  # pending, in_progress, completed, error
    progress: Optional[str]
    filepath: Optional[str]

@app.get("/status")
def status():
    return Response(status_code = 200)


@app.post("/download", response_model=DownloadStatus)
def start_download(request: DownloadRequest):
    # Generate a unique ID for the download
    download_id = str(uuid.uuid4())
    downloads[download_id] = {"status": "pending", "filepath": None, "progress": "0%", "start_time": time.time()}

    # Prepare the command based on request
    output_file = os.path.join(DOWNLOAD_DIR, f"{download_id}.%(ext)s")
    end_or_length = request.end_or_length if request.end_or_length else ""
    if request.type == "video_start_end":
        command = [
            "yt-dlp",
            f"--download-sections=*{request.start}-{end_or_length}",
            "-f", "bestvideo+bestaudio",
            request.url,
            "-o", output_file
        ]
    elif request.type == "video_start_length":
        command = [
            "yt-dlp",
            f"--download-sections=*{request.start}+{end_or_length}",
            "-f", "bestvideo+bestaudio",
            request.url,
            "-o", output_file
        ]
    elif request.type == "audio_start_end":
        command = [
            "yt-dlp",
            f"--download-sections=*{request.start}-{end_or_length}",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            request.url,
            "-o", output_file
        ]
    elif request.type == "audio_start_length":
        command = [
            "yt-dlp",
            f"--download-sections=*{request.start}+{end_or_length}",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            request.url,
            "-o", output_file
        ]
    else:
        raise HTTPException(status_code=400, detail="Invalid download type")

    # Run the command in a separate thread
    def run_download():
        downloads[download_id]["status"] = "in_progress"
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                # Update progress based on yt-dlp output
                if "[download]" in line and "%" in line:
                    progress = line.split("%")[0].split()[-1] + "%"
                    downloads[download_id]["progress"] = progress
            process.wait()
            if process.returncode == 0:
                downloads[download_id]["status"] = "completed"
                downloads[download_id]["filepath"] = output_file.replace("%(ext)s", "mp4" if "video" in request.type else "mp3")
            else:
                downloads[download_id]["status"] = "error"
        except Exception as e:
            downloads[download_id]["status"] = "error"

    threading.Thread(target=run_download).start()

    return DownloadStatus(id=download_id, status="pending", progress="0%", filepath=None)

@app.put("/download/{download_uuid}")
def put_start_download(download_uuid:UUID4, request: YTVideoDownloadRequest):
    return Response(status_code = 202)


@app.get("/download/{download_id}", response_model=DownloadStatus)
def check_status(download_id: str):
    if download_id not in downloads:
        raise HTTPException(status_code=404, detail="Download ID not found")

    download_info = downloads[download_id]

    if download_info["status"] == "completed":
        # Check if 15 minutes have passed since completion
        if time.time() - download_info["start_time"] > 900:
            filepath = download_info.get("filepath")
            if filepath and os.path.exists(filepath):
                os.remove(filepath)
            downloads.pop(download_id, None)
            raise HTTPException(status_code=404, detail="Download expired")

    return DownloadStatus(
        id=download_id,
        status=download_info["status"],
        progress=download_info.get("progress", "0%"),
        filepath=None if download_info["status"] != "completed" else download_info["filepath"]
    )

@app.get("/download/{download_id}/file")
def download_file(download_id: str):
    if download_id not in downloads:
        raise HTTPException(status_code=404, detail="Download ID not found")

    download_info = downloads[download_id]

    if download_info["status"] != "completed":
        raise HTTPException(status_code=400, detail="File not ready for download")

    filepath = find_file_by_id(download_id)

    if not filepath or not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")

    # Determine the MIME type based on file extension
    mime_type, _ = mimetypes.guess_type(filepath)
    if not mime_type:
        mime_type = "application/octet-stream"

    # Send the file without removing it immediately
    response = FileResponse(filepath, media_type=mime_type, filename=os.path.basename(filepath))

    # Remove the file in a background thread after sending
    def remove_file():
        time.sleep(1)  # Allow the response to complete
        if os.path.exists(filepath):
            os.remove(filepath)

    threading.Thread(target=remove_file).start()

    downloads.pop(download_id, None)
    return response

# Background cleanup thread for expired downloads
def cleanup_expired_downloads():
    while True:
        time.sleep(60)
        now = time.time()
        expired_ids = [
            download_id for download_id, info in downloads.items()
            if info["status"] == "completed" and now - info["start_time"] > 900
        ]
        for download_id in expired_ids:
            filepath = downloads[download_id].get("filepath")
            if filepath and os.path.exists(filepath):
                os.remove(filepath)
            downloads.pop(download_id, None)

threading.Thread(target=cleanup_expired_downloads, daemon=True).start()
