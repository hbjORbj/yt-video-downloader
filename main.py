import os
from yt_dlp import YoutubeDL
import argparse
from typing import List

def download_video(video_url: str, output_folder="downloads", verbose=False) -> str:
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
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(output_folder, '%(title)s_%(upload_date>%Y_%m_%d)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'verbose': verbose,
        'nocheckcertificate': True,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print(f"\nDownloading video: {video_url}")
            info = ydl.extract_info(video_url, download=True)
            if info:
                video_title = info.get('title', 'Unknown')
                upload_date = info.get('upload_date', '')
                if upload_date:
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

def process_download_queue(urls: List[str], output_folder="downloads", verbose=False) -> List[str]:
    """
    Process a queue of video URLs and download them sequentially.

    Args:
        urls (List[str]): List of YouTube video URLs to download.
        output_folder (str): Folder to save the downloaded videos.
        verbose (bool): Enable verbose output for debugging.

    Returns:
        List[str]: List of paths to successfully downloaded video files.
    """
    successful_downloads = []
    failed_downloads = []

    print(f"\nProcessing download queue: {len(urls)} videos")
    for i, url in enumerate(urls, 1):
        print(f"\nProcessing video {i}/{len(urls)}")
        result = download_video(url.strip(), output_folder, verbose)
        if result:
            successful_downloads.append(result)
        else:
            failed_downloads.append(url)

    # Print summary
    print("\nDownload Queue Summary")
    print("=====================")
    print(f"Total videos: {len(urls)}")
    print(f"Successfully downloaded: {len(successful_downloads)}")
    print(f"Failed downloads: {len(failed_downloads)}")
    
    if failed_downloads:
        print("\nFailed URLs:")
        for url in failed_downloads:
            print(f"- {url}")

    return successful_downloads

def get_urls_from_input() -> List[str]:
    """Get multiple URLs from user input."""
    print("Enter YouTube URLs (one per line)")
    print("Press Enter twice when done:")
    
    urls = []
    while True:
        url = input().strip()
        if not url:
            break
        urls.append(url)
    return urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Video Downloader with Queue Support")
    parser.add_argument("-u", "--urls", nargs="+", help="YouTube video URLs to download")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-o", "--output", default="downloads", help="Output folder path")
    args = parser.parse_args()

    print("YouTube Video Downloader")
    print("========================")

    # Get URLs either from command line arguments or user input
    urls_to_process = args.urls if args.urls else get_urls_from_input()

    if urls_to_process:
        process_download_queue(urls_to_process, args.output, args.verbose)
    else:
        print("No URLs provided. Exiting.")