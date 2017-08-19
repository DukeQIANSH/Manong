import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl = "https://www.facebook.com/ShayneElliottANZ"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

print(soup.title.text)
print(soup.find('div',{"class":"_4bl9"}).text)

"""
for link in soup.findAll('a'):
    print(link.get('href'))
    print(link.text)
"""

i=1
for fbs in soup.findAll('div',{"class":"_1dwg _1w_m"}):
    print(i)
    print("发布时间:" + fbs.find('abbr').text) #发布时间
    print("发布内容:" + fbs.find('p').text) #发布内容
    #print(fbs.find('href'))
    i = i+1

