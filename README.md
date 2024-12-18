# YouTube Video Downloader

A Python-based script to download the highest-quality YouTube videos, complete with audio and video merged into an MP4 file.

## Features

- Downloads YouTube videos in the highest available resolution.
- Ensures audio and video are merged into a single MP4 file.
- Simple and user-friendly.

## Requirements

- Python 3.7 or higher
- `yt-dlp` library
- `ffmpeg` (must be installed and accessible in your system's PATH)

## Installation

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/hbjORbj/yt-video-downloader.git
   cd yt-video-downloader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install `ffmpeg`:
   - **Linux**: Use your package manager, e.g., `sudo apt install ffmpeg`.
   - **MacOS**: Install via Homebrew: `brew install ffmpeg`.
   - **Windows**: Download and install from [FFmpeg.org](https://ffmpeg.org).

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Enter the YouTube video URL when prompted.

3. The video will be downloaded and saved in the `downloads` folder.

## Output

- Videos are saved in the `downloads` folder by default.
- File format: `.mp4`

## Example

```plaintext
YouTube Video Downloader
========================
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Downloading video...
Downloaded: downloads/Never Gonna Give You Up.mp4
Video successfully downloaded to: downloads/Never Gonna Give You Up.mp4
```

## Legal Disclaimer

This script is intended for personal use and should only be used to download videos that you own or have permission to download. Downloading copyrighted content without authorization may violate YouTube's Terms of Service and applicable copyright laws.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
