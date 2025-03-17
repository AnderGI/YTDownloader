from src.contexts.backoffice.youtubevideo.domain.YoutubeVideo import YoutubeVideo
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoExtractor import YoutubeVideoExtractor
from src.contexts.backoffice.youtubevideo.application.DownloadYoutubeVideoCommand import DownloadYoutubeVideoCommand

class YoutubeVideoDownloader:
  def __init__(self, extractor:YoutubeVideoExtractor) -> None:
    self.extractor = extractor

  def run(self, command:DownloadYoutubeVideoCommand) -> None:
    _ = YoutubeVideo.create(id=command.id, url=command.url, start=command.start, end=command.end)
    self.extractor.extract(_)