from pytube import YouTube
filename="musicList.txt"
file=open(filename,"r")

for videoURL in file:
    print(videoURL)
    yt = YouTube(videoURL)
    stream = yt.streams.first()
    stream.download("/home/dio/Music/")
    print('下載完成')
    #print("輸入網址錯誤")
