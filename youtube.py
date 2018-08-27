from pytube import YouTube
while 1:
    videoname=input("輸入youtube網址:\n")
    try:
        yt = YouTube(videoname)
        stream = yt.streams.first()
        stream.download("/home/dio/music/favorite/")
        print('下載完成')
    except:
        print("輸入網址錯誤")
