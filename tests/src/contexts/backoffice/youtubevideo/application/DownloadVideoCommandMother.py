from src.contexts.backoffice.youtubevideo.application.DownloadYoutubeVideoCommand import DownloadYoutubeVideoCommand
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict


class DownloadVideoCommandMother:
    @staticmethod
    def create(
        id: str,
        start: YoutubeVideoTimestampDict, 
        end: YoutubeVideoTimestampDict
    ) -> DownloadYoutubeVideoCommand:  
        return DownloadYoutubeVideoCommand(id=id, start=start, end=end)
    