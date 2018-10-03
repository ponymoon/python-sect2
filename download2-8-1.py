from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base =  "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="
quote = rep.quote_plus("케로로") #유니코드로변환
url = base + quote
res = req.urlopen(url)
savepath = "C:\\imagedown\\" #C:/imagedown/

try:
    if not (os.path.isdir(savepath)):
        os.makedirs(os.path.join(savepath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.img_area._item > a.thumb._thumb > img")
for i, img_list in enumerate(img_list,1):
    #print(img_list['data-source'])
    fullfilename = os.path.join(savepath, savepath+str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'],fullfilename)
