import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgurl ="http://blogfiles.naver.net/20160916_216/vetmed01_1474024130918XAg3f_JPEG/cat-1669567_960_720.jpg"
htmlurl ="http://google.com"

savepath1 ="c:/test1.jpg"
savepath2 ="c:/index.html"

dw.urlretrieve(imgurl,savepath1)
dw.urlretrieve(htmlurl,savepath2)

print('다운로드완료')
