from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict

    
class YoutubeVideoEndRange:
    def __init__(self, time: YoutubeVideoTimestampDict):
        self._validate_time_dict(time)
        self.hour = time["hour"]
        self.minute = time["minute"]
        self.second = time["second"]

    def _validate_time_dict(self, time: YoutubeVideoTimestampDict):
        if not (0 <= time["hour"] < 24):
            raise ValueError("Hour must be between 0 and 23")
        if not (0 <= time["minute"] < 60):
            raise ValueError("Minute must be between 0 and 59")
        if not (0 <= time["second"] < 60):
            raise ValueError("Second must be between 0 and 59")

    def to_seconds(self) -> int:
        return self.hour * 3600 + self.minute * 60 + self.second