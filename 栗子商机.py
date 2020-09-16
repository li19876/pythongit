# coding=utf-8
"""
Author:song
"""
import json
import random

import time

import nb_print
import pymysql
import requests
import tools
db = pymysql.connect(host="127.0.0.1",port = 3306,user="root",password="li123456..",db="lys",charset="utf8")
cursor=db.cursor()
def run(keyword='天津教育',page=1,diqu=''):
    url="https://www.clues.cn/api/gonghai/clickContact?pid={}&from=gonghai"
    listurl='https://www.clues.cn/api/opensearch/search'
    header="""Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZjViMjFlNTNhM2UyYjc5NDBmYTk4ZDMiLCJyb2xlIjoibWFpbmFjY291bnQiLCJzZXF1ZW5jZSI6MCwiZHRNb2JpbGVTZXF1ZW5jZSI6MCwic3RhdHVzIjoxLCJkaXNhYmxlIjpmYWxzZSwidHlwZSI6OCwiYWdlbnRfdHlwZSI6MCwiYWdlbnRfaWQiOiIiLCJkdHlwZSI6NCwiaWF0IjoxNTk5ODA3OTczLCJleHAiOjE2MDAwOTkxOTl9.bOn3F7UCuvzoN1Fj7AQJQE2BM7U8BUvA4dsBsXrLCLk
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 436
Content-Type: application/json;charset=UTF-8
Host: www.clues.cn
Origin: https://www.clues.cn
Pragma: no-cache
Referer: https://www.clues.cn/search
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
X-AK-UID: 5f470ed5e858dc6285677c32"""
    headers=tools.make_header(header)
    cookie="""_uab_collina=159849310298267446399272; Hm_lvt_52ec34d38adb4a7123e14a20870d743a=1598492300,1599795024; gotopc=true; Hm_lpvt_52ec34d38adb4a7123e14a20870d743a=1599807999"""
    cookies=tools.make_cookie(cookie)
    # with open('sj.json',encoding='utf-8') as j:
    #     data=j.readline()
    # aa=json.dumps(data)
    data={"keyword": keyword,"filter": "{\"location\":[\"%s\"],\"industryshort\":[],\"registercapital\":\"0\",\"establishment\":\"0\",\"entstatus\":\"1\",\"enttype\":\"0\",\"contact\":[\"1001\"],\"finance\":[\"all\"],\"trademark\":\"0\",\"patent\":\"0\",\"shixin\":\"0\",\"tenders\":\"0\",\"mobileApp\":\"0\",\"sem\":\"0\",\"scale\":\"0\",\"website\":\"0\",\"employment\":\"0\",\"highTech\":\"0\"}" % diqu,"scope": "","sortType": 0,"pagesize": 50,"page": page}

    # print(data)
    res= requests.post(listurl,json=data,cookies=cookies,headers=headers)
    return res.text
def save(item):
    try:
        sql="""insert into lizi (companyname,address,businessAddress,entstatus,enttype,pid,industry,legalperson,province,regcapcur,registercapital,scale1) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        data=[item['value'],item['address'],item['businessAddress'],item['entstatus'],item['enttype'],item['id'],item['industry'],item['legalperson'],item['province'],item['regcapcur'],item['registercapital'],item['scale']]
        # sql2 = """insert into lizi_contact (pid) values (%s)"""
        cursor.execute(sql, data)
        # cursor.execute(sql2,item['id'])


    except Exception as e:
        db.rollback()
        print(e)
    else:
        db.commit()
        print(item['value'] + '写入完成')
def parse(res):
    cop=json.loads(res)
    items= cop['data']['items']
    for item in items:
        save(item)

if __name__=='__main__':

    keyword='餐饮'
    diqunum=["120101","120102","120103","120104","120105","120106","120110","120111","120112","120113","120114","120115","120116","120117","120118","120119"]
    for d in diqunum:
        print("开始抓取地区："+d)
        res = json.loads(run(keyword, 1,d))
        num=res['data']['total']
        flag=0
        if num>=5000:
            flag=101
        elif num <5000:
            flag=num//50+2
        elif num==0:
            print('无结果，下一地区')
            continue
        print('一共%d页，开始抓取' % flag)
        for i in range(1,flag):
            print(str(i)+'页开始抓取')
            res=run(keyword,i,d)
            parse(res)
            print(str(i) + '页抓取完成')
            time.sleep(random.randint(1,3))

