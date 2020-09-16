# coding=utf-8
"""
Author:song
"""
import datetime
import json
import random
import getip
import time
import urllib.parse
import nb_print
import pymysql
import requests
import tools
db = pymysql.connect(host="127.0.0.1",port = 3306,user="root",password="li123456..",db="lys",charset="utf8")
cursor=db.cursor()
def getres(pid,cop):
    url="https://www.clues.cn/api/gonghai/clickContact?pid={}&from=market"
    header="""Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZjQ3MGVkNWU4NThkYzYyODU2NzdjMzIiLCJyb2xlIjoibWFpbmFjY291bnQiLCJzZXF1ZW5jZSI6MSwiZHRNb2JpbGVTZXF1ZW5jZSI6MCwic3RhdHVzIjoxLCJkaXNhYmxlIjpmYWxzZSwidHlwZSI6OCwiYWdlbnRfdHlwZSI6MCwiYWdlbnRfaWQiOiIiLCJkdHlwZSI6NCwiaWF0IjoxNTk5ODEzODY0LCJleHAiOjE2MDA0NDQ3OTl9.RmQjsTUp5SuFREGNsyhBfB8qbVhKmuYN3q65l2bUkbQ
Cache-Control: no-cache
Connection: keep-alive
Host: www.clues.cn
Pragma: no-cache
Referer: https://www.clues.cn/sea
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
X-AK-UID: 5f470ed5e858dc6285677c32"""
    headers=tools.make_header(header)
    cookie="""_uab_collina=159849229971967678447844; Hm_lvt_52ec34d38adb4a7123e14a20870d743a=1598492300,1599795024; gotopc=true; Hm_lpvt_52ec34d38adb4a7123e14a20870d743a=1599813858"""
    cookies=tools.make_cookie(cookie)
    # with open('sj.json',encoding='utf-8') as j:
    #     data=j.readline()
    # aa=json.dumps(data)
    # print(type(aa))
    res= requests.get(url.format(pid),cookies=cookies,headers=headers)
    # print(res.text)
    # exit()
    return json.loads(res.text)
def save(res,pid,cop):

    items=res['data']['item']
    for item in items:
        label=item['label']
        value=item['value']
        address=item['data'][0]['address']
        sourceName=item['data'][0]['sourceName']
        qq=item['data'][0]['qq']
        email = item['data'][0]['email']
        url= item['data'][0]['URL']
        contact= item['data'][0]['contact']
        companyname=cop
        sql="""insert into lizi_contact (pid,label,value1,address,sourceName,qq,email,url,contact,companyname,datetime) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        data=[pid,label,value,address,sourceName,qq,email,url,contact,companyname,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        try:
            cursor.execute(sql,data)
            print('写入：'+cop)
        except Exception as e:
            db.rollback()
            print(e)
    db.commit()


def run():
    sql="SELECT pid,companyname from lizi where pid not in (select pid from lizi_contact) and industry = '住宿和餐饮业'"
    cursor.execute(sql)
    aa=cursor.fetchall()
    print('数据库查询完成')
    for pid,cop in aa:
        res=getres(pid,cop)
        print(res)
        # with open('log.txt','a') as log:
        #     log.write(str(res))
        save(res,pid,cop)
        # time.sleep(float("0."+str(random.randint(1,9))))
        time.sleep(3)
if __name__=="__main__":
    run()