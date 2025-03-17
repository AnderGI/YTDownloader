from src.contexts.backoffice.youtubevideo.application.DownloadYoutubeVideoCommand import DownloadYoutubeVideoCommand

class DownloadVideoCommandMother:
    @staticmethod
    def createValidCommand() -> DownloadYoutubeVideoCommand:  
        return DownloadYoutubeVideoCommand(id="6b682748-6bbf-46aa-a6a8-702bc8996a33",start={"hour": 1, "minute": 20, "second": 30}, end={"hour": 1, "minute": 45, "second": 15})
    