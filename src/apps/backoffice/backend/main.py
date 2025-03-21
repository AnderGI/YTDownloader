from fastapi import FastAPI, Response
from pydantic import BaseModel, UUID4, HttpUrl, Field
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict
from src.contexts.backoffice.youtubevideo.application.YoutubeVideoDownloader import YoutubeVideoDownloader
from src.contexts.backoffice.youtubevideo.infrastructure.YTDLPYoutubeVideoExtractor import YTDLPYoutubeVideoExtractor 
from src.contexts.backoffice.youtubevideo.application.DownloadYoutubeVideoCommand  import DownloadYoutubeVideoCommand
import os

app = FastAPI()

# Directory to store downloaded files
DOWNLOAD_DIR = "downloads"

class TimeStampVideo(BaseModel):
    hour: int = Field(ge=0, lt=24, description="Hours (0-23)")
    minute: int = Field(ge=0, lt=60, description="Minutes (0-59)")
    second: int = Field(ge=0, lt=60, description="Seconds (0-59)")

class YTVideoDownloadRequest(BaseModel):
    url: HttpUrl
    start: TimeStampVideo
    end: TimeStampVideo

@app.get("/status")
def status():
    return Response(status_code=200)

@app.put("/download/{download_uuid}")
def put_start_download(download_uuid: UUID4, request: YTVideoDownloadRequest):
    start: YoutubeVideoTimestampDict = {
        "hour": int(request.start.hour),
        "minute": int(request.start.minute),
        "second": int(request.start.second)
    }

    end: YoutubeVideoTimestampDict = {
        "hour": int(request.end.hour),
        "minute": int(request.end.minute),
        "second": int(request.end.second)
    }

    try:
        extractor = YTDLPYoutubeVideoExtractor()
        downloader = YoutubeVideoDownloader(extractor)
        command = DownloadYoutubeVideoCommand(download_uuid.hex,str(request.url), start, end)
        downloader.run(command)
        return Response(status_code=202)
    except ValueError:
        return Response(status_code=406)
    

@app.get("/download/status/{video_id}")
def get_download_status(video_id: str):
    video_id = video_id.replace('-', '')
    download_dir = os.path.join(os.getenv("PYTHONPATH", os.getcwd()), "downloads")
    output_file = os.path.join(download_dir, f"{video_id.replace('-', '')}.mp3")
    
    if os.path.exists(output_file):
        return {"video_id": video_id, "status": "completed"}
    else:
        return {"status": "404 Not Found"}