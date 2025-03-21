from src.contexts.backoffice.youtubevideo.application.DownloadYoutubeVideoCommand import DownloadYoutubeVideoCommand
from faker import Faker
class DownloadVideoCommandMother:
    @staticmethod
    def createValidCommand() -> DownloadYoutubeVideoCommand:  
        fake = Faker()
        return DownloadYoutubeVideoCommand(id=fake.uuid4(),url = fake.url() ,start={"hour": 1, "minute": 20, "second": 30}, end={"hour": 1, "minute": 45, "second": 15})
    