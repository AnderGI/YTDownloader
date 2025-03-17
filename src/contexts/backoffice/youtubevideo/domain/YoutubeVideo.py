from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampRange import YoutubeVideoTimestampRange
from typing import TypedDict

class YoutubeVideoTimestampPrimitive(TypedDict):
    hour: int
    minute: int
    second: int

class YoutubeVideoPrimitive(TypedDict):
    id: str
    url: str
    start: YoutubeVideoTimestampPrimitive
    end: YoutubeVideoTimestampPrimitive

class YoutubeVideo:
    def __init__(self, id: str,url:str, timestamp_range: YoutubeVideoTimestampRange):
        self.id = id
        self.url = url
        self.timestamp_range = timestamp_range

    @staticmethod
    def create(id: str, url:str, start: YoutubeVideoTimestampDict, end: YoutubeVideoTimestampDict) -> 'YoutubeVideo':
        timestamp_range = YoutubeVideoTimestampRange(start=start, end=end)
        return YoutubeVideo(id, url, timestamp_range=timestamp_range)


    def to_primitives(self) -> YoutubeVideoPrimitive:
        return {
            "id": self.id,
            "url":self.url,
            "start": {
                "hour": self.timestamp_range.start_range.hour,
                "minute": self.timestamp_range.start_range.minute,
                "second": self.timestamp_range.start_range.second,
            },
            "end": {
                "hour": self.timestamp_range.end_range.hour,
                "minute": self.timestamp_range.end_range.minute,
                "second": self.timestamp_range.end_range.second,
            },
        }
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, YoutubeVideo):
            return False
        return self.id == value.id
