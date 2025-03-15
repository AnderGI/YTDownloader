from abc import ABC, abstractmethod
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideo import YoutubeVideo


class YoutubeVideoExtractor(ABC):
  @abstractmethod
  def extract(self, _:YoutubeVideo)->None:
    pass