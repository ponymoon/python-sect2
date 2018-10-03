# 네이버 배너광고 다운
import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url1 = "https://ssl.pstatic.net/tveta/libs/1191/1191683/67695b8ac77faba784c4_20180928143548242.jpg"
url2 = "https://tvetamovie.pstatic.net/libs/1209/1209123/53f4a3f17534befb3347_20180910094357270.mp4-pBASE-v0-f63850-20180910094457793_4.mp4"

k1 = req.urlopen(url1).read()
k2 = req.urlopen(url2).read()

path1 = 'c:/test그림.jpg'
path2 = 'c:/test영상.mp4'

with open(path1,'wb') as savefile1:
    savefile1.write(k1)
with open(path2,'wb') as savefile1:
    savefile1.write(k2)
