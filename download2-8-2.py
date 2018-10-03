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

base =  "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌") #유니코드로변환
url = base + quote
res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())
savepath = "C:\\imagedown\\" #C:/imagedown/
try:
    if not (os.path.isdir(savepath)):
        os.makedirs(os.path.join(savepath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("ul.slides")[0]

for i, e in enumerate(img_list,1):
    with open(savepath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("h4.block_title > a").string)
    fullfilename = os.path.join(savepath, savepath+str(i)+'.png')
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullfilename)

print("다운로드 완료")
