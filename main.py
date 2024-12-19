import os
from yt_dlp import YoutubeDL
import sys

def download_video(video_url, output_folder="downloads", verbose=False):
    """
    Downloads a YouTube video using yt-dlp and forces MP4 output.
    Filename format: title_YYYY_MM_DD.mp4

    Args:
        video_url (str): The URL of the YouTube video to download.
        output_folder (str): Folder to save the downloaded video.
        verbose (bool): Enable verbose output for debugging.

    Returns:
        str: Path to the downloaded video file.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        # Force MP4 output
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',  # Force merging into MP4
        'outtmpl': os.path.join(output_folder, '%(title)s_%(upload_date>%Y_%m_%d)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Ensure final format is MP4
        }],
        'verbose': verbose,
        'nocheckcertificate': True,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print("Downloading video (forcing MP4 format)...")
            info = ydl.extract_info(video_url, download=True)
            if info:
                video_title = info.get('title', 'Unknown')
                upload_date = info.get('upload_date', '')
                if upload_date:
                    # Format: title_YYYY_MM_DD.mp4
                    formatted_date = f"{upload_date[:4]}_{upload_date[4:6]}_{upload_date[6:8]}"
                    video_file = os.path.join(output_folder, f"{video_title}_{formatted_date}.mp4")
                else:
                    video_file = os.path.join(output_folder, f"{video_title}.mp4")
                print(f"Successfully downloaded: {video_file}")
                return video_file

    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        if verbose:
            import traceback
            print("Full error traceback:")
            traceback.print_exc()
        return None

if __name__ == "__main__":
    print("YouTube Video Downloader")
    print("========================")

    verbose_mode = "--verbose" in sys.argv or "-v" in sys.argv
    video_url = input("Enter the YouTube video URL: ").strip()

    if video_url:
        downloaded_file = download_video(video_url, verbose=verbose_mode)
        if not downloaded_file:
            print("\nTroubleshooting steps:")
            print("1. Make sure ffmpeg is installed on your system")
            print("2. Try updating yt-dlp: yt-dlp -U")
            print("3. Check if the video is accessible in your browser")
    else:
        print("No URL provided. Exiting.")