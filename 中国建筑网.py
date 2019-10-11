import requests
import pymysql
from lxml import etree
import time
import re
from fake_useragent import UserAgent
ua = UserAgent()
s = requests.session()
s.keep_alive = False
db = pymysql.connect(host="127.0.0.1",port = 3306,user="root",password="li123456..",db="lys",charset="utf8")
cursor=db.cursor()

def geturllist(url="https://yp.cbi360.net/yp/List/?EnterpriseTypeID=8&p=",pagenum=40):
    urllist=[]
    for i in range(1,pagenum+1):
        urllist.append(url+str(i))
    return urllist

def run():
    ua = UserAgent()
    headers={"user-agent":ua.random,'Connection': 'close'}
    urllist = geturllist()
    print(urllist)
    for url in urllist:
        print("进入"+url)
        res= requests.get(url,headers=headers)
        html =etree.HTML(res.text)
        gslist = html.xpath("//div[@class='countdown_div']")
        for gs in gslist:
            gsname = gs.xpath(".//tbody/tr[1]/td/span/a/text()")[0].strip()
            lxr = gs.xpath("string(.//tbody/tr[2]/td/p[1])").replace(" ","")
            lxdh = gs.xpath("string(.//tbody/tr[2]/td/p[2])").replace(" ","")
            try:
                print("开始写入")
                sql = """
                    insert into jzw(gsname,lxr,lxdh,city) values ('{}','{}','{}','{}')
                """.format(gsname,lxr,lxdh,gsname[0:2])
                cursor.execute(sql)
                db.commit()
                print("写入了:{},{},{},{}".format(gsname,lxr,lxdh,gsname[0:2]))
            except:
                db.rollback()
        time.sleep(1)
if __name__== '__main__':
    run()