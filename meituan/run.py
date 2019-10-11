import csv
import time
import threading
from get_cookies import get_cookie
from get_cookies import parse
import getip
import pymysql


def crow(n, l):  # 参数n 区分第几个线程，l存储url的列表+
    db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="li123456..", db="lys", charset="utf8")
    cursor = db.cursor()
    lock = threading.Lock()
    sym = 0  # 是否连续三次抓取失败的标志位
    pc = get_cookie()  # 获取IP 和 Cookie
    m = 0  # 记录抓取的数量
    now = time.time()
    while True:
        if len(l) > 0:
            u = l.pop(0)
            # print(u)
            # exit()
            ll = len(l)
            m += 1
            ttt = time.time() - now

            result = parse(u, pc, m, n, ll, ttt)
            mark = result[0]
            info = result[1]
            if mark == 2:
                time.sleep(1.5)
                result = parse(u, pc, m, n, ll, ttt)
                mark = result[0]
                info = result[1]
                if mark != 0:
                    sym += 1
            if mark == 1:
                pc = get_cookie(1)
                result = parse(u, pc, m, n, ll, ttt)
                mark = result[0]
                info = result[1]
                if mark != 0:
                    sym += 1
            if mark == 0:  # 抓取成功
                sym = 0
                # with open('meituan.csv', 'a', newline='', encoding='gb18030')as f:
                #     write = csv.writer(f)
                #     write.writerow(info)
                # f.close()
                lock.acquire()
                try:

                    save(info)


                except Exception as e:
                    print("写入异常:",e)
                    db.rollback()
                lock.release()
            if sym > 2:  # 连续三次抓取失败，换ip、cookie
                sym = 0
                pc = get_cookie(1)
            time.sleep(3)
            print("休息3s")
        else:
            print('&&&&线程：%d结束' % n)
            break

def save(info):
    sql = """
        update meituan set address='{}',phone='{}',perprice='{}',businesshours='{}',star='{}',
        speaknum='{}',status='1',pub1='{}',pub2='{}' where id = '{}'
    """.format(info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10],info[0])
    db.ping(reconnect=True)
    cursor.execute(sql)
    db.commit()
if __name__ == '__main__':
    db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="li123456..", db="lys", charset="utf8")
    cursor = db.cursor()
    url_list = []
    sql ="""
        select name,category,poiid,ctpoi,id from meituan where status=''
    """
    cursor.execute(sql)
    res=cursor.fetchall()
    for line in res:
        # print(line)
        d_list = ['', '','']
        url = 'https://meishi.meituan.com/i/poi/' + str(line[2]) + '?ct_poi=' + str(line[3])
        d_list[0] = url
        d_list[1] = line[1]
        d_list[2] = line[4]
        url_list.append(d_list)

    th_list = []
    for i in range(1, 2):
        t = threading.Thread(target=crow, args=(i, url_list,))
        print('*****线程%d开始启动...' % i)
        t.start()
        th_list.append(t)
        time.sleep(40)
    for t in th_list:
        t.join()
