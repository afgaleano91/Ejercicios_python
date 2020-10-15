from urllib import request
from bs4 import BeautifulSoup

html=request.urlopen('http://py4e-data.dr-chuck.net/comments_866756.html').read()
sopa = BeautifulSoup(html)
tags=sopa('span')
result=0
for tag in tags:
    result=result+int(tag.contents[0])
print(result)