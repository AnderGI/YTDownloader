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
