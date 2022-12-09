from pytube import YouTube
link = input("paste your link here : ")
yt = YouTube(link)
print(f"you are about to download {yt.title} video")
quality = int(input("""
Enter in Which Quality you want to download the video

1) 360p
2) 720p
3) 1080p

"""))

if quality == 1:
    itag = 18
elif quality == 2:
    itag = 22
else:
    itag = 137
stream = yt.streams.get_by_itag(itag)

stream.download()
print('download completed successfully!')
