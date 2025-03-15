from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoStartRange import YoutubeVideoStartRange
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoEndRange import YoutubeVideoEndRange
from typing import TypedDict

class YoutubeVideoTimestampPrimitive(TypedDict):
    hour: int
    minute: int
    second: int

class YoutubeVideoPrimitive(TypedDict):
    id: str
    start: YoutubeVideoTimestampPrimitive
    end: YoutubeVideoTimestampPrimitive


class YoutubeVideo:
    def __init__(self, id: str, start: YoutubeVideoTimestampDict, end: YoutubeVideoTimestampDict):
        self.id = id;
        self.start_range = YoutubeVideoStartRange(start)
        self.end_range = YoutubeVideoEndRange(end)
        self._validate_range()

    @staticmethod
    def create(id: str,
        start: YoutubeVideoTimestampDict, 
        end: YoutubeVideoTimestampDict) -> 'YoutubeVideo':
        _ = YoutubeVideo(id=id, start=start, end=end)
        return _

    def _validate_range(self):
        if self.start_range.to_seconds() >= self.end_range.to_seconds():
            raise ValueError("Start time must be earlier than end time")

    def to_primitives(self) -> YoutubeVideoPrimitive:
        return {
            "id" : self.id,
            "start": {
                "hour": self.start_range.hour,
                "minute": self.start_range.minute,
                "second": self.start_range.second,
            },
            "end": {
                "hour": self.end_range.hour,
                "minute": self.end_range.minute,
                "second": self.end_range.second,
            },
        }
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, YoutubeVideo):
            return False
        return self.id == value.id
