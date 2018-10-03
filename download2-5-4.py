from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html><body>
<div id="main">
    <h1>강의목록</h1>
    <ul class="lecs">
        <li>java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html,'html.parser')

#h1 = soup.select("div#main > h1")
#print('h1',h1)

#for z in h1:
    #print(z.string)      즉 select로추출한것은 리스트형식이다!
h1 = soup.select_one("div#main > h1")
print('h1',h1.string)

list_li = soup.select("div#main > ul.lecs > li")
for l in list_li:
    print("l>>",l.string)
