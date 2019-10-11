import requests
from lxml import etree
import pymysql
import random
import time
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()
def getres(page=1):
    url = "http://www.fynas.com/ua/search?d=&b=&k=&page="+str(page)
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"}
    res = requests.get(url,headers=headers)
    html = etree.HTML(res.text)
    uas = html.xpath("//table[@class='table table-bordered']/tr")
    ualist=[]
    for i in uas:
        ua = i.xpath("string(.//td[4])")
        ualist.append(ua)
    return ualist[1:]


if __name__ =='__main__':
    # for i in range(30):
    #     res = getres(i)
    #     for ua in res:
    #         sql = """
    #             INSERT into useragent(ua) VALUES ("{}")
    #         """.format(ua)
    #         curosr.execute(sql)
    #     db.commit()
    #     time.sleep(1)
    #     print("休息1s")
    id = random.randint(1, 111)
    sql = "select *from useragent where id = {}".format(id)
    curosr.execute(sql)
    res = curosr.fetchall()
    print(res[0][1])