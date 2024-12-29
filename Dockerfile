FROM python:3.9

# Set the working directory
WORKDIR /app

# Disable interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and clean up
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    python3 \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir yt-dlp fastapi uvicorn

# Ensure the downloads directory exists
RUN mkdir -p downloads

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Instructions for Docker in README.md:
# 1. Build the Docker image:
#    ```bash
#    docker build -t yt-dlp-api .
#    ```
# 2. Run the Docker container:
#    ```bash
#    docker run -d -p 8000:8000 yt-dlp-api
#    ```
# 3. Access the application at: http://127.0.0.1:8000
