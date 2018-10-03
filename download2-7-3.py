from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base =  "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌") #유니코드로변환

url = base + quote

res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset()) #euc-kr 쓰므로 'euc-kr'이라해도 된다
soup = BeautifulSoup(res,"html.parser")

recommend = soup.select("ul.slides")[0]
for i,e in enumerate(recommend,1):
    print(i, e.select_one("h4.block_title > a").string)
