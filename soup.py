import urllib.request,urllib.parse,urllib.error
from bs4 import BeutifulSoup
url=input('http://www.dr-chuck.com/page1.htm')
html=urllib.request.request.urlopen(url).read()
soup=BeutifulSoup(html,'html.parser')

tags=soup('a')
for tag in tags:
    print('href',None)
