import time
import requests
import json
import pymysql
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()

url = "http://www.xiongmaodaili.com/xiongmao-web/api/glip?secret=23225551106b6bfd49129dcc97f0c91b&orderNo=GL20190620165705pPDVsNCm&count=1&isTxt=1&proxyType=1"
def getip(refalsh=0):
    now = int(time.time())
    sec = """
            select * from proxies order by id desc limit 0,1
        """
    curosr.execute(sec)
    ss = curosr.fetchall()
    if (int(ss[0][2])-5 <= now) or refalsh==1:

        while 1:
            ip = requests.get(url).text
            try:
                re = requests.get("http://icanhazip.com",proxies={"http":ip[0:-2]})
                if re.status_code == 200:
                    insert = """
                                insert into proxies(ip,guoqitime) values ('{}','{}')
                    """.format(ip[0:-2], now + 300)
                    curosr.execute(insert)
                    db.commit()
                    print("发生过期或者错误新获取一个ip")
                    return ip[0:-2]
                else:
                    raise NameError
            except Exception as e:
                print(str(e))

    else:
        try:
            re = requests.get("http://icanhazip.com", proxies={"http": ss[0][1]})
            if re.status_code == 200:
                print("返回一个数据库的ip")
                return ss[0][1]
            else:
                getip(1)
        except Exception as e:
            getip(1)

if __name__ == '__main__':
    print(getip())
