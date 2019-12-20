import time

import requests
from lxml import etree
import pymysql
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()

def getres(url):
    headers= {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'referer':url,
        'Connection':'keep-alive',
        'host':'www.y80s.com',
        'Upgrade-Insecure-Requests':'1',
        'Cache-Control':'no-cache',
        'Pragma':'no-cache'
    }
    cookie = 'Hm_lvt_e55ff7844747a41e412fd2b38266f729=1576221916; UM_distinctid=16efe25c66f536-02005b902e8493-6c247613-1aeaa0-16efe25c670a84; Hm_lvt_e4476baf9a1725eedfe34c443331f6cf=1576221928; CNZZDATA1274572815=1600196122-1576220151-http%253A%252F%252Fwww.y80s.com%252F%7C1576230951; Hm_lpvt_e55ff7844747a41e412fd2b38266f729=1576232578; Hm_lpvt_e4476baf9a1725eedfe34c443331f6cf=1576232578'
    cookies = {i.split('=')[0]:i.split('=')[1] for i in cookie.split('; ')}
    res = requests.get(url,headers=headers,cookies=cookies)
    if res.status_code != 200:
        print(res.status_code)
        return False
    return res

def parse(url):
    while True:
        res = getres(url)
        if len(res.text)>1000:
            html = etree.HTML(res.text)
            mvlist = html.xpath('//*[@id="block1"]/ul')

            print(mvlist)
            alist = mvlist[0].xpath('.//li/a/@href')
            alink=[]
            for s in alist:
                alink.append("http://www.y80s.com"+s)
            # print(alist)
            titlelist = mvlist[0].xpath('.//li/a/@title')
            return list(zip(alink,titlelist))
        print(res.text)
        print("访问失败,休息4s")
        time.sleep(4)

def save(item):
    movie_name = item[1]
    link = item[0]
    sql = """
        insert into 80smovie(movie_name,link) values ('{}','{}')
    """.format(movie_name,link)
    curosr.execute(sql)
    try:
        db.commit()
        print('写入了:',item)
    except Exception as e:
        db.rollback()
        print("入库错误:",str(e))

if __name__=='__main__':
    urllist=[]
    for i in range(134,177):
        urllist.append('http://www.y80s.com/movie/list/---2--p'+str(i))
    for url in urllist:
        print(url)
        items=parse(url)

        for item in items:
            save(item)
        time.sleep(2)
