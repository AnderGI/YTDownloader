from src.contexts.backoffice.youtubevideo.domain.YoutubeVideo import YoutubeVideo
from src.contexts.backoffice.youtubevideo.application.DownloadYoutubeVideoCommand import DownloadYoutubeVideoCommand

class YoutubeVideoMother:
    @staticmethod
    def from_command(
        command:DownloadYoutubeVideoCommand
    ) -> YoutubeVideo:  
        return YoutubeVideo.create(id=command.id,url= command.url, start=command.start, end=command.end)
    
   