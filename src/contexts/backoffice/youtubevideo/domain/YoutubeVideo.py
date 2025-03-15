from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoStartRange import YoutubeVideoStartRange
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoEndRange import YoutubeVideoEndRange

class YoutubeVideo:

    def __init__(self, start: YoutubeVideoTimestampDict, end: YoutubeVideoTimestampDict):
        self.start_range = YoutubeVideoStartRange(start)
        self.end_range = YoutubeVideoEndRange(end)
        self._validate_range()

    def _validate_range(self):
        if self.start_range.to_seconds() >= self.end_range.to_seconds():
            raise ValueError("Start time must be earlier than end time")

    def to_primitives(self):
        return {
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
