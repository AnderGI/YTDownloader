from fastapi import FastAPI, Response
from pydantic import BaseModel, UUID4, HttpUrl, Field

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
    return Response(status_code=202)
