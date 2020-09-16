import time
import requests
import sendemail
import pymysql
import selenium
import threading
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()
lock = threading.Lock()
url = "http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=23225551106b6bfd49129dcc97f0c91b&orderNo=GL20200827155629sfDw0K93&count=1&isTxt=1&proxyType=1"
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
        except Exception as e:
            print("获取数据库ip时发生错误",str(e))
            ip=getnew()
            return ip
def getnew():

    while True:
        try:
            now = int(time.time())
            beforehour = now -3600
            select ="""
                select * from proxies where guoqitime < {} and guoqitime > {}
            """.format(now+300,beforehour)
            num=curosr.execute(select)
            print("一小时内获取的ip数是:",num)
            # print(type(num))
            # exit()
            if num>=100:
                sendemail.sendemail("li.yansong@hzsr-media.com", "IP异常获取", "1小时内获取了超过100IP")
                return False
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

def getmore():
    url = 'http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=23225551106b6bfd49129dcc97f0c91b&orderNo=GL20190620165705pPDVsNCm&count=10&isTxt=1&proxyType=1'
    res = requests.get(url).text
    res = res.split('\n')[:-1]
    now = int(time.time())
    for i in res:
        insert = """
                 insert into proxies_copy(ip,guoqitime) values ('{}','{}')
                 """.format(i, now + 300)
        curosr.execute(insert)
    try:
        db.commit()
        print("获取成功")
    except Exception as e:
        print(str(e))

def getone():
    now = int(time.time())
    beforehour = now - 3600
    select = """
                    select id,ip from proxies_copy where guoqitime < {} and guoqitime > {}
                """.format(now + 300, beforehour)
    curosr.execute(select)
    ip=curosr.fetchone()
    if ip is None:
        getmore()
        now = int(time.time())
        beforehour = now - 3600
        select = """
                            select id,ip from proxies_copy where guoqitime < {} and guoqitime > {}
                        """.format(now + 300, beforehour)
        curosr.execute(select)
        ip = curosr.fetchone()
    dele = 'delete from proxies_copy where id = "{}"'.format(ip[0])
    curosr.execute(dele)
    db.commit()
    return ip[1][:-1]
if __name__ == '__main__':
    print(getip())
