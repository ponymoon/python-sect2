from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url =  "https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset()) #euc-kr 쓰므로 'euc-kr'이라해도 된다
soup = BeautifulSoup(res,"html.parser")

top5 = soup.select("#siselist_tab_0 > tr")

i=1
for e in top5:
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string)
        i+=1
