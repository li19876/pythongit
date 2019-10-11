import requests
from lxml import etree
url = "http://b2b.huangye88.com/guangdong/huagong/"
headers= {"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

res = requests.get(url,headers=headers)
html=etree.HTML(res.text)
shiurl =html.xpath("//div[@class='adr_hot adr_hot2']/a/@href")
qurl=[]
for s in shiurl:
    res = requests.get(s, headers=headers)
    html = etree.HTML(res.text)
    quurl = html.xpath("//div[@class='adr_hot adr_hot2']/a/@href")
    print(quurl)
    qurl+=quurl
with open("quurl.txt","a",encoding="utf-8") as f:
    for i in qurl:
        f.write(i+"\n")