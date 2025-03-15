from unittest.mock import Mock
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoExtractor import YoutubeVideoExtractor
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideo import YoutubeVideo

class MockYoutubeVideoExtractor(YoutubeVideoExtractor):
    def __init__(self):
        self.extract_mock = Mock()
        self.extracted_video = None
    
    def extract(self, _:YoutubeVideo) -> None:
        self.extracted_video = _
        self.extract_mock(_)
    
    def assert_extract_called_with_video(self, expected_video:YoutubeVideo) -> None:
        self.extract_mock.assert_called_once()
        assert self.extracted_video == expected_video, "The video passed to extractor doesn't match the expected video"

