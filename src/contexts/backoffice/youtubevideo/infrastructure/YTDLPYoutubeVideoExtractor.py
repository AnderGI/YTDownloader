from src.contexts.backoffice.youtubevideo.domain.YoutubeVideoExtractor import YoutubeVideoExtractor
from src.contexts.backoffice.youtubevideo.domain.YoutubeVideo import YoutubeVideo
from subprocess import Popen, PIPE, STDOUT
import threading
import os

class YTDLPYoutubeVideoExtractor(YoutubeVideoExtractor):
    def __init__(self):
      self.download_dir = os.path.join(os.getenv("PYTHONPATH", os.getcwd()), "downloads")
      os.makedirs(self.download_dir, exist_ok=True) 
      pass

    def extract(self, _: YoutubeVideo) -> None:
        if any(_.id in filename for filename in os.listdir(self.download_dir)):
            return
        start_time = "{:02d}:{:02d}:{:02d}".format(
            _.timestamp_range.start_range.hour,
            _.timestamp_range.start_range.minute,
            _.timestamp_range.start_range.second
        )
        end_time = "{:02d}:{:02d}:{:02d}".format(
            _.timestamp_range.end_range.hour,
            _.timestamp_range.end_range.minute,
            _.timestamp_range.end_range.second
        )
        
        command: list[str] = [
            "yt-dlp",
            f"--download-sections=*{start_time}-{end_time}",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            _.url,
            "-o",
            os.path.join(self.download_dir, f"{_.id}")
        ]

        threading.Thread(target=self._run_download, args=(command,)).start()

    def _run_download(self, command:list[str]):
        try:
            process: Popen[str] = Popen(command, stdout=PIPE, stderr=STDOUT, text=True)
            if process.stdout is not None:
                for line in process.stdout:  # Leer la salida en tiempo real
                    print(line.strip())
            process.wait()
        except Exception as e:
            print(f"Error en la descarga: {e}")
