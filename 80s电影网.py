import time
import re
import requests
from lxml import etree
import pymysql
import getip
from fake_useragent import UserAgent
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()
ua = UserAgent()

def getres(url):
    headers= {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'User-Agent':ua.random,
        'referer':url,
        'Connection':'keep-alive',
        'host':'www.y80s.com',
        'Upgrade-Insecure-Requests':'1',
        'Cache-Control':'no-cache',
        'Pragma':'no-cache'
    }
    cookie = 'Hm_lvt_e55ff7844747a41e412fd2b38266f729=1576221916; UM_distinctid=16efe25c66f536-02005b902e8493-6c247613-1aeaa0-16efe25c670a84; Hm_lvt_e4476baf9a1725eedfe34c443331f6cf=1576221928; CNZZDATA1274572815=1600196122-1576220151-http%253A%252F%252Fwww.y80s.com%252F%7C1576230951; Hm_lpvt_e55ff7844747a41e412fd2b38266f729=1576232578; Hm_lpvt_e4476baf9a1725eedfe34c443331f6cf=1576232578'
    cookies = {i.split('=')[0]:i.split('=')[1] for i in cookie.split('; ')}
    while True:
        try:
            res = requests.get(url,headers=headers,cookies=cookies,proxies={'http':"http://"+getip.getip()},timeout=5)
            return res
        except Exception as e:
            print("访问出错,休息3S,错误信息:",str(e))
            time.sleep(3)
            continue

def check(res):
    return res[0].replace("'","").replace('"','') if res else ''

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

def parse_datail(url):
    res = getres(url)
    thunder = re.findall(r"thunderHref=\"(.+)\">迅雷下载</A>", res.text)
    thunder = check(thunder)
    downname = re.findall(r'thunderresTitle=\"(.+?)\"',res.text,re.IGNORECASE)
    downname = check(downname)
    downlink = re.findall(r'a\shref=\"(.+mp4)\".+>本地下载',res.text)
    downlink = check(downlink)
    star = re.findall(r'评分：</span>\s+<span class="score sc\d+" ></span>(\d\.\d)',res.text)
    star = check(star)
    return {"thunder":thunder,"downname":downname,"downlink":downlink,"star":star}

def save(item):
    movie_name = item[1]
    link = item[0]
    sql = """
        insert into 80smovie(movie_name,link) values ('{}','{}')
    """.format(movie_name,link)

    try:
        curosr.execute(sql)
        db.commit()
        print('写入了:',item)
    except Exception as e:
        db.rollback()
        print("入库错误:",str(e))

def update(item,id):
    sql = """
        update 80smovie set downlink = '{}' ,downname = '{}' ,thunder = '{}', star = '{}' where id = '{}'
    """.format(item["downlink"],item["downname"],item["thunder"],item["star"],id)
    # print(sql)
    curosr.execute(sql)
    try:
        db.commit()
        print("写入成功:",item["downname"])
    except Exception as e:
        db.rollback()
        print("回滚事务:",str(e))

if __name__=='__main__':
    # 获取大概
    # urllist=[]
    # for i in range(729):
    #     urllist.append('http://www.y80s.com/movie/list/-----p'+str(i))
    # for url in urllist:
    #     print(url)
    #     items=parse(url)
    #
    #     for item in items:
    #         save(item)
    #     time.sleep(2)
    # 获取详情
    sql = """
        select id,link from 80smovie where thunder IS NULL
    """
    curosr.execute(sql)
    allres = curosr.fetchall()
    # print(allres)
    for i in allres:
        print(i)
        res=parse_datail(i[1])
        update(res,i[0])
        time.sleep(2)
    #     # break
