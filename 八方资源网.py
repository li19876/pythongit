import requests
import pymysql
from lxml import etree
import time
import re
# from fake_useragent import UserAgent
# ua = UserAgent()
s = requests.session()
s.keep_alive = False
db = pymysql.connect(host="127.0.0.1",port = 3306,user="root",password="li123456..",db="lys",charset="utf8")
cursor=db.cursor()
def parse(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",'Connection': 'close'}

    res = requests.get(url,headers=headers)
    html = etree.HTML(res.text)
    pagenum = html.xpath("//div[@class='pages']/text()")[0]
    pagenum = int(re.findall(r"\d\d?",pagenum)[0])
    gsname = html.xpath("//ul[@class='list']/li/div[@class='biaoti']/a/text()")
    lxfs = html.xpath("//ul[@class='list']/li/div[@class='n_r']/p[@class='gs_n gs_name']/span[1]/text()")
    res = list(zip(gsname, lxfs))
    res.append(pagenum)
    return res
#获取详情列表页链接
def geturllist(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/69.0.3497.100 Safari/537.36",'Connection': 'close'
               }
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    href = html.xpath("//ul[@class='app_list']/li/a/@href")
    url=[]
    for s in href:
        url.append("https://www.b2b168.com"+s)
    url.remove("https://www.b2b168.com/xiaofang/xiaofangqicai/yingjizhaomingdeng/")
    return url

def run():
    beginurl = "https://www.b2b168.com/xiaofang/xiaofangqicai/"
    zurllist = geturllist(beginurl)#详情列表页链接列表
    print(zurllist)
    for baba in zurllist:
        pagenum = parse(baba)[-1] #取当前分类总页数
        urllist=[]
        for ss in range(1,pagenum+1):
            urllist.append("{}l-{}.html".format(baba,ss)) #获取翻页链接列表
        print(urllist)

        for url in urllist:
            for i in parse(url)[:-1]:
                sql ="""
                    insert into bfzy(gsname,lxfs) values ('{}','{}')
                """.format(i[0],i[1])
                cursor.execute(sql)
                db.commit()
                print("写入了:"+i[0]+i[1])

            time.sleep(3)
            print("查完一页,休息3s")
        time.sleep(5)
        print("查完一类,休息5s")
if __name__ == "__main__":
    run()
    cursor.close()
    db.close()