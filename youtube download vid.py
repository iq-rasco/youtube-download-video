from pytube import YouTube

print('Download video from web by python:')
url = input('Enter video url: ')
yt = YouTube(url)
yt.streams.get_highest_resolution().download('tools')
