from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideo import YoutubeVideo
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoExtractor import YoutubeVideoExtractor


class YoutubeVideoDownloader:
  def __init__(self, extractor:YoutubeVideoExtractor) -> None:
    self.extractor = extractor
    

  def run(self, start: YoutubeVideoTimestampDict, end: YoutubeVideoTimestampDict) -> None:
    _ = YoutubeVideo(start=start, end=end)
    self.extractor.extract(_)