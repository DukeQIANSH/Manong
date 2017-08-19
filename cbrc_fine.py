#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
#主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询

import urllib
import urllib.request
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url= "http://www.cbrc.gov.cn/chinese/home/docView/86D21EFE646D450D8B99D96CAABC6F41.html", headers=headers)
thepage = urllib.request.urlopen(req).read()

soup = BeautifulSoup(thepage,"html.parser")
body = soup.find_all('div', {"class":"Section1"})

print(soup.title.text)

for div in body:
    print(div.text)



