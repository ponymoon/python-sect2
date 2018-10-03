from urllib.parse import urljoin

baseurl = "http://test.com/html/a.html"
print(">>", urljoin(baseurl, "b.html"))
print(">>", urljoin(baseurl, "sub/b.html"))
print(">>", urljoin(baseurl, "../index.html"))
