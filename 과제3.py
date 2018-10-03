from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url =  "https://www.daum.net"

res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset()) #euc-kr 쓰므로 'euc-kr'이라해도 된다
soup = BeautifulSoup(res,"html.parser")

list_10 = soup.find_all("a", tabindex="-1")
for i,k in enumerate(list_10,1):
    print(i,'.','검색어 :', k.string,'link주소 :', k.attrs['href'])

#ol.list_hotissue issue_row list_mini
#span.txt_issue
#for k in list_10:
