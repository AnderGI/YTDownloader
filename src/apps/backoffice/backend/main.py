from fastapi import FastAPI, Response
from pydantic import BaseModel, UUID4, HttpUrl, Field
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict
from src.contexts.backoffice.youtubevideo.application.YoutubeVideoDownloader import YoutubeVideoDownloader
from src.contexts.backoffice.youtubevideo.infrastructure.YTDLPYoutubeVideoExtractor import YTDLPYoutubeVideoExtractor 

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
        downloader.run(start, end)
        return Response(status_code=202)
    except ValueError:
        return Response(status_code=406)