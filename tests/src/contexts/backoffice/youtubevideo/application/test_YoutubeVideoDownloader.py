from src.contexts.backoffice.youtubevideo.application.YoutubeVideoDownloader import YoutubeVideoDownloader
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoTimestampDict import YoutubeVideoTimestampDict 
from tests.src.contexts.backoffice.youtubevideo.infrastructure.MockYoutubeVideoExtractor import MockYoutubeVideoExtractor
from tests.src.contexts.backoffice.youtubevideo.domain.YoutubeVideoMother import YoutubeVideoMother


def test_youtube_video_downloader_happy_path():
    # Arrange
    start_range:YoutubeVideoTimestampDict = {"hour": 1, "minute": 20, "second": 30}
    end_range:YoutubeVideoTimestampDict = {"hour": 1, "minute": 45, "second": 15}
    
    extractor = MockYoutubeVideoExtractor()
    downloader = YoutubeVideoDownloader(extractor)
    
    # Act
    downloader.run("6b682748-6bbf-46aa-a6a8-702bc8996a33",start_range, end_range)
    video = YoutubeVideoMother.create("6b682748-6bbf-46aa-a6a8-702bc8996a33",start_range, end_range)

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