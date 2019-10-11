import time
import requests
import json
import pymysql
import threading
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()
lock = threading.Lock()
url = "http://www.xiongmaodaili.com/xiongmao-web/api/glip?secret=23225551106b6bfd49129dcc97f0c91b&orderNo=GL20190620165705pPDVsNCm&count=1&isTxt=1&proxyType=1"
def getip(refalsh=0):
    now = int(time.time())
    sec = """
            select * from proxies order by id desc limit 0,1
        """
    lock.acquire()
    curosr.execute(sec)
    lock.release()
    ss = curosr.fetchall()
    if (int(ss[0][2])-5 <= now) or refalsh==1:
    #获取新ip
        lock.acquire()
        ip=getnew()
        lock.release()
        return ip
    else:
        try:
            re = requests.get("http://icanhazip.com", proxies={"http": ss[0][1]},timeout=(3,10))
            print("返回一个数据库的ip")
            return ss[0][1]
        except TimeoutError:
            print("数据库ip链接超时,获取新ip")
            ip=getnew()
            return ip
        except Exception as e:
            print("获取数据库ip时发生错误",str(e))
            ip=getnew()
            return ip
def getnew():

    while True:
        try:
            now = int(time.time())
            ip = requests.get(url).text
            re = requests.get("http://icanhazip.com", proxies={"http": ip[0:-2]}, timeout=(3, 10))
            insert = """
                insert into proxies(ip,guoqitime) values ('{}','{}')
            """.format(ip[0:-2], now + 300)

            curosr.execute(insert)

            db.commit()
            print("新获取了一个ip:"+ip[:-2])
            return ip[:-2]

        except TimeoutError:
            print("新ip连接超时,重新获取")
            time.sleep(1)
        except Exception as e:
            print("新获取的ip发生错误")
            print(str(e))
            time.sleep(2)

if __name__ == '__main__':
    print(getip())
