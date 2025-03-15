from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoExtractor import YoutubeVideoExtractor
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideo import YoutubeVideo

class YTDLPYoutubeVideoExtractor(YoutubeVideoExtractor):
  def __init__(self):
    pass

  def extract(self, _: YoutubeVideo) -> None:
    # Your implementation here
    print(_)
    print("Extracting videos using yt-dlp")
    # Do actual extraction work...