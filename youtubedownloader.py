from pytube import YouTube 

videolink=str(input("Link of The Youtube video :"))
yt = YouTube(videolink)
yd=yt.streams.get_highest_resolution()
yd.download(r"your path to save the video")
