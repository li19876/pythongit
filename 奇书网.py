# -- coding: utf-8 --
import requests
import re
from urllib import request,parse
from lxml import etree
def geturllist(url="https://www.qisuu.la/soft/sort01/"):
    response = requests.get(url)
    html = etree.HTML(response.text)
    lilist = html.xpath("//div[@class='listBox']/ul/li")
    urllist = []
    for li in lilist:
        a = li.xpath(".//a/@href")
        urllist.append("https://www.qisuu.la"+a[0])
    print(urllist)
    return urllist

def getdownurl():
    urllist = geturllist()
    downlist =[]
    for i in urllist:

        detail = requests.get(i)
        print("进入"+i)
        deahtml=etree.HTML(detail.text.encode(detail.encoding).decode(detail.apparent_encoding))
        print(detail.text.encode(detail.encoding).decode(detail.apparent_encoding))

        downurl = deahtml.xpath("//div[@class='showDown']/ul/li[3]/script/text()")
        url=re.findall(r"https://.+\.txt",downurl[0])
        # print(url)
        downloadfile(url[0])
        break
        # downlist.append(url)
    print(downlist)
def downloadfile(url):
    filename = url.split("/")[-1]
    with open(filename,"w",encoding="utf-8") as f:
        for s in requests.get(url).text:
            try:
                f.write(s)
                print("写入了："+s)
            except:
                continue
if __name__ == "__main__":
    getdownurl()
