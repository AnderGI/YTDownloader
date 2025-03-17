from src.contexts.backoffice.youtubevideo.application.YoutubeVideoDownloader import YoutubeVideoDownloader
from tests.src.contexts.backoffice.youtubevideo.infrastructure.MockYoutubeVideoExtractor import MockYoutubeVideoExtractor
from tests.src.contexts.backoffice.youtubevideo.domain.YoutubeVideoMother import YoutubeVideoMother
from tests.src.contexts.backoffice.youtubevideo.application.DownloadVideoCommandMother import DownloadVideoCommandMother

def test_youtube_video_downloader_happy_path():
    extractor = MockYoutubeVideoExtractor()
    downloader = YoutubeVideoDownloader(extractor)
    command = DownloadVideoCommandMother.createValidCommand()
    # Act
    downloader.run(command)
    video = YoutubeVideoMother.from_command(command)
    # Assert
    extractor.assert_extract_called_with_video(video)

"""
def test_youtube_video_downloader_invalid_range():
    # Arrange
    start_timestamp = {"hour": 2, "minute": 0, "second": 0}
    end_timestamp = {"hour": 1, "minute": 30, "second": 0}
    
    extractor = MockYoutubeVideoExtractor()
    downloader = YoutubeVideoDownloader(extractor)
    
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        downloader.run(start_timestamp, end_timestamp)
    
    assert "Start time must be earlier than end time" in str(excinfo.value)
    assert not extractor.extract_mock.called
"""