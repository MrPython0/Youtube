from pytube import YouTube
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules('pytube')

video_link = input("paste the link here: \n")

video = YouTube(video_link)

print("Video Title: \n", video.title)
print("video Length: \n", video.length)
print("video Views: \n", video.views)
print("video description: \n", video.description)

video.streams.get_highest_resolution().download(output_path="C:/Users/anas/Downloads")

def finish():
    print("download done !")


video.register_on_complete_callback(finish())