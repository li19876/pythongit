import pymysql
import random
import threading
lock = threading.Lock()
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()
def randua():
    id = random.randint(1, 18521)
    sql = "select *from useragent where id = {}".format(id)
    lock.acquire()
    curosr.execute(sql)
    lock.release()
    uas = curosr.fetchall()[0][1]
    # print("当前获取的UA是:"+uas)
    return uas
