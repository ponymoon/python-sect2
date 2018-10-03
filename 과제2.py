import pytube
import os
import subprocess

yturl = input("다운받으실 유튜브주소를 입력하세요")
yt = pytube.YouTube(yturl) #다운받을 동영상 url 지정
videos = yt.streams.all()

#print('videos',videos)

for i in range(len(videos)):
    print(i, ',', videos[i])

cnum=int(input("다운받을화질?(0~17 입력)",))
down_dir = "c:/utube"

videos[cnum].download(down_dir)
k = input("mp3로 변환하시겠습니까?(y/n)")
if k=="y":
    newfilename = input("변환할 mp3이름?")
    orifilename = videos[cnum].default_filename

    subprocess.call(['ffmpeg','-i', os.path.join(down_dir,orifilename),
    os.path.join(down_dir,newfilename)])

    print("동영상, mp3다운 완료")
else:
    print("동영상만 다운 완료")
