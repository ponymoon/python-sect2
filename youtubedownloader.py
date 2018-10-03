import pytube
import os
import subprocess

yt = pytube.YouTube("https://www.youtube.com/watch?v=yutfHiV13o0") #다운받을 동영상 url 지정
videos = yt.streams.all()

#print('videos',videos)

for i in range(len(videos)):
    print(i, ',', videos[i])

cnum=int(input("다운받을화질?(0~17 입력)"))
down_dir = "c:/utube"

videos[cnum].download(down_dir)

newfilename = input("변환할 mp3이름?")
orifilename = videos[cnum].default_filename

subprocess.call(['ffmpeg','-i', os.path.join(down_dir,orifilename),
os.path.join(down_dir,newfilename)])

print("동영상, mp3다운 완료")
