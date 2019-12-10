import requests
from lxml import etree
url = "https://www.b2b168.com/jiaoyu/xuelijiaoyu/"
headers= {"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

res = requests.get(url,headers=headers)
html=etree.HTML(res.text)
shiurl =html.xpath("//ul[@class='app_list']/li/a/@href")
for i in shiurl:
    print("https://www.b2b168.com"+i)
