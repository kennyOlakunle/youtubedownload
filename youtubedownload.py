import yt_dlp


save_path = '/Users/yourname/Downloads/'
video_url = 'https://www.youtube.com/watch?v=your_video_id'


# Function to download YouTube video and convert to MP3 in best quality
def download_best_audio_as_mp3(video_url, save_path=save_path):
    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save path and file name
        'postprocessors': [{  # Post-process to convert to MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to mp3
            'preferredquality': '0',  # '0' means best quality, auto-determined by source
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Example usage
download_best_audio_as_mp3(video_url, save_path)



# # Function to download YouTube playlist using yt-dlp
# def download_playlist(playlist_url, save_path=save_path):
#     ydl_opts = {
#         'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save path
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([playlist_url])




# download_playlist(playlist_url, save_path)
