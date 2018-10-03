import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

api = "https://api.ipify.org"

val = {'format' : 'json'}
print('before',val)
params = urlencode(val)
print('after',params)

url = api + "?" + params
print("요청 url",url)

reqdata=req.urlopen(url).read().decode('utf-8')
print("출력", reqdata)
