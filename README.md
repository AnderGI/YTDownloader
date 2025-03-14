# YTDownloader 🎥🎵✨

## Overview 🌟📂💻

This project is a FastAPI-based API that enables downloading video and audio segments from a given URL using `yt-dlp`. The API supports various download modes and allows users to track download progress, retrieve the status, and download the resulting file. Files are automatically removed after being downloaded or if not retrieved within 15 minutes of completion. 🚀🕒✅

## Features 🌈⚙️📋

- Download video or audio segments by specifying start and end times or duration.
- Track the progress and status of downloads.
- Automatically delete files after download or expiration.
- File management and cleanup handled seamlessly in the background. 🔄🗂️✨

## ToDo List

- [ ] Fix Dockerfile
- [ ] Fix Trim Videos (video is unsynced when using --download-section in `yt-dlp`)
- [ ] Add X, TikTok & Instagram options

## Installation 🔧📥📦

### Prerequisites ⚠️🛠️🧰

- Python 3.8 or higher
- `yt-dlp` installed. You can install it with:
  ```bash
  pip install yt-dlp
  ```
- `FastAPI` and `uvicorn` installed. Install them using:
  ```bash
  pip install fastapi uvicorn
  ```

### Setup 📁📜🖥️

1. Clone the repository or copy the code to your local machine.
2. Navigate to the project directory.
3. Create a Virtual Environment:

```bash
 python -m venv venv
```

4. Activate the Virtual Environment:

- Windows:
  ```bash
    venv\\Scripts\\activate
  ```
- Mac/Linux:
  ```bash
    source venv/bin/activate
  ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure the `downloads` directory exists:
   ```bash
   mkdir downloads
   ```

### Docker setup 🐋

1. Build the Docker image:
   ```bash
   docker build -t yt-downloader .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 yt-downloader
   ```
3. Access the application at: http://127.0.0.1:8000

## Usage 📡💾📤

### Start the API 🏁🚀📡

Run the FastAPI server with `uvicorn`:

```bash
uvicorn main:app --reload


uvicorn src.apps.backoffice.backend.main:app --reload

```

By default, the server will run at `http://127.0.0.1:8000`. 🌐📍⚡

### Endpoints 🛣️📩📬

#### 1. Start a Download ⬇️🎬🎶

**POST** `/download`

Initiate a download with the following payload:

```json
{
  "url": "URL_TO_VIDEO",
  "start": "START_TIME",
  "end_or_length": "END_TIME_OR_DURATION",
  "type": "video_start_end | video_start_length | audio_start_end | audio_start_length"
}
```

```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "start": "1:00:00",
  "end_or_length": "0:01:20",
  "type": "video_start_end"
}
```

- **`url`**: The video URL.
- **`start`**: Start time (e.g., `00:01:00` for 1 minute).
- **`end_or_length`**: End time or duration (e.g., `00:02:00` for 2 minutes).
- **`type`**: Specify the mode of download:
  - `video_start_end`: Video from start to end.
  - `video_start_length`: Video from start for a given duration.
  - `audio_start_end`: Audio from start to end.
  - `audio_start_length`: Audio from start for a given duration.

Example response:

```json
{
  "id": "unique-download-id",
  "status": "pending",
  "progress": "0%",
  "filepath": null
}
```

#### 2. Check Download Status 🔍📊🕵️

**GET** `/download/{download_id}`

Retrieve the status of a download by providing the `download_id` from the response of the start download request.

Example response:

```json
{
  "id": "unique-download-id",
  "status": "in_progress",
  "progress": "45%",
  "filepath": null
}
```

#### 3. Download the File 📁📥💾

**GET** `/download/{download_id}/file`

Download the completed file by providing the `download_id`. The file will be removed from the server after successful retrieval. ✅📤🗑️

#### 4. Automatic Cleanup 🧹🕒💨

Completed downloads will be automatically removed if not downloaded within 15 minutes. ⏳🚫🗂️

## Background Cleanup 🔄🗑️🌌

The application uses a background thread to periodically remove expired files and free up storage. ♻️📉✨

## License 📜🖋️🔓

This project is under no License because "no valen para una mierda salu2".
