# YouTube Video to MP3 Downloader

This script downloads audio from a YouTube video and converts it to MP3 format using `yt-dlp` and `FFmpeg`.

## Prerequisites
1. Install Python:
Ensure you have Python 3 installed. You can download it from [Python.org](https://www.python.org/).

2. Install yt-dlp:
Use pip to install `yt-dlp`:
```
pip install yt-dlp

```
3. Install `FFmpeg`:
FFmpeg is required for audio conversion.

- macOS (using Homebrew)
```
brew install ffmpeg
```
- Windows: Download FFmpeg from [here](https://ffmpeg.org/download.html) and follow the installation instructions.

## Usage
### Modify the Script:
Set the `video_url` and `save_path` to your desired YouTube video URL and save location.

#### Example Code:
```
import yt_dlp

save_path = '/Users/yourname/Downloads/'
video_url = 'https://www.youtube.com/watch?v=your_video_id'

def download_best_audio_as_mp3(video_url, save_path=save_path):
    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Run the function
download_best_audio_as_mp3(video_url, save_path)
```


## Running the Script
1. Open a terminal or command prompt.
2. Run the script using Python:
```
python your_script_name.py
```


The MP3 file will be saved to the specified `save_path`.



### License
This project is open-source and licensed under the `MIT License`.
