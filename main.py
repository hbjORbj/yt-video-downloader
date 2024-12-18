import os
from yt_dlp import YoutubeDL

def download_video(video_url, output_folder="downloads"):
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        video_url (str): The URL of the YouTube video to download.
        output_folder (str): Folder to save the downloaded video.

    Returns:
        str: Path to the downloaded video file.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # yt-dlp options for downloading
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Highest quality video and audio
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Save path and naming pattern
        'merge_output_format': 'mp4',  # Ensure output is in mp4 format
        'postprocessors': [{
            'key': 'FFmpegMerger',  # Merge video and audio
        }]
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_title = info.get('title', 'Unknown')
            video_file = os.path.join(output_folder, f"{video_title}.mp4")
            print(f"Downloaded: {video_file}")
            return video_file
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

if __name__ == "__main__":
    print("YouTube Video Downloader")
    print("========================")

    # Get video URL input
    video_url = input("Enter the YouTube video URL: ").strip()

    if video_url:
        print("Downloading video...")
        downloaded_file = download_video(video_url)

        if downloaded_file:
            print(f"Video successfully downloaded to: {downloaded_file}")
        else:
            print("Failed to download the video.")
    else:
        print("No URL provided. Exiting.")
