# YouTube Video Downloader

A Python-based script to download the highest-quality YouTube videos, complete with audio and video merged into an MP4 file.

## Features

- Downloads YouTube videos in the highest available resolution
- Ensures audio and video are merged into a single MP4 file
- Supports downloading multiple videos in a queue
- Saves videos with upload date in the filename (YYYY_MM_DD format)
- Command-line interface with multiple options
- Interactive mode for entering multiple URLs
- Simple and user-friendly

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
   - **Linux**: Use your package manager, e.g., `sudo apt install ffmpeg`
   - **MacOS**: Install via Homebrew: `brew install ffmpeg`
   - **Windows**: Download and install from [FFmpeg.org](https://ffmpeg.org)

## Usage

### Command-line Interface

The script supports various command-line arguments:

```bash
python main.py [-h] [-u URLS [URLS ...]] [-v] [-o OUTPUT]

Optional arguments:
  -h, --help            Show this help message and exit
  -u, --urls URLS [URLS ...]
                        YouTube video URLs to download
  -v, --verbose         Enable verbose output
  -o, --output OUTPUT   Output folder path (default: 'downloads')
```

### Examples

1. Download a single video:
   ```bash
   python main.py -u https://youtube.com/watch?v=example
   ```

2. Download multiple videos:
   ```bash
   python main.py -u https://youtube.com/watch?v=example1 https://youtube.com/watch?v=example2
   ```

3. Specify output folder:
   ```bash
   python main.py -u https://youtube.com/watch?v=example -o my_videos
   ```

4. Enable verbose output:
   ```bash
   python main.py -u https://youtube.com/watch?v=example -v
   ```

### Interactive Mode

1. Run the script without arguments:
   ```bash
   python main.py
   ```

2. Enter YouTube URLs one per line
3. Press Enter twice when done
4. Videos will be downloaded sequentially

## Output

- Videos are saved in the `downloads` folder by default (can be changed with `-o` option)
- File format: `title_YYYY_MM_DD.mp4`
- Example: `Never Gonna Give You Up_2009_10_25.mp4`

## Example Output

```plaintext
YouTube Video Downloader
========================
Processing download queue: 2 videos

Processing video 1/2
Downloading video: https://youtube.com/watch?v=example1
Successfully downloaded: downloads/Video Title 1_2024_01_15.mp4

Processing video 2/2
Downloading video: https://youtube.com/watch?v=example2
Successfully downloaded: downloads/Video Title 2_2024_01_15.mp4

Download Queue Summary
=====================
Total videos: 2
Successfully downloaded: 2
Failed downloads: 0
```

## Legal Disclaimer

This script is intended for personal use and should only be used to download videos that you own or have permission to download. Downloading copyrighted content without authorization may violate YouTube's Terms of Service and applicable copyright laws.

## License

This project is licensed under the MIT License. See the LICENSE file for details.