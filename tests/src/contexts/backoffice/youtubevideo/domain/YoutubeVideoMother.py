from src.contexts.backoffice.youtubevideo.domain.YoutubeVideo import YoutubeVideo
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict

class YoutubeVideoMother:
    @staticmethod
    def create(
        id: str,
        start: YoutubeVideoTimestampDict, 
        end: YoutubeVideoTimestampDict
    ) -> YoutubeVideo:  
        return YoutubeVideo(uuid=id, start=start, end=end)
    
   