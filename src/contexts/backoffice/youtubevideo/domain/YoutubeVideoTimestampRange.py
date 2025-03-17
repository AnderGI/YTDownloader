from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoStartRange import YoutubeVideoStartRange
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoEndRange import YoutubeVideoEndRange


class YoutubeVideoTimestampRange:
    def __init__(self, start: YoutubeVideoTimestampDict, end: YoutubeVideoTimestampDict):
        self.start_range = YoutubeVideoStartRange(start)
        self.end_range = YoutubeVideoEndRange(end)
        self._validate_range()
    
    @staticmethod
    def create(start: YoutubeVideoTimestampDict, end: YoutubeVideoTimestampDict) -> 'YoutubeVideoTimestampRange':
        return YoutubeVideoTimestampRange(start=start, end=end)
    
    def _validate_range(self) -> None:
        if self.start_range.to_seconds() >= self.end_range.to_seconds():
            raise ValueError("Start time must be earlier than end time")