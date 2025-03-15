from dataclasses import dataclass
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict

@dataclass
class DownloadYoutubeVideoCommand:
    id: str
    start: YoutubeVideoTimestampDict
    end: YoutubeVideoTimestampDict
    
    @classmethod
    def create(cls, id: str, start: YoutubeVideoTimestampDict, end: YoutubeVideoTimestampDict) -> 'DownloadYoutubeVideoCommand':
        return cls(id=id, start=start, end=end)