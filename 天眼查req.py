import requests
from fake_useragent import UserAgent
from lxml import etree
import random
import csv
import time
import pymysql
ua = UserAgent()
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()
#获取响应
#参数为要查询的公司名
def getres(keyword= "北京皓智顺然"):

    url ="https://www.tianyancha.com/search?key="+keyword

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'www.tianyancha.com',
        'Referer':'https://www.tianyancha.com/search?key=%E5%A4%A9%E6%B4%A5%E6%95%99%E8%82%B2',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':ua.random
    }
    #c     = 'jsid=SEM-BAIDU-PP-VI-000873; TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; aliyungf_tc=AQAAAIHF7VU/tAMAvn4vajbCkcsjt5Kh; bannerFlag=undefined; csrfToken=CjTQs6nrjHmjMUNT0kPY8eLU; _gid=GA1.2.656427539.1562044105; token=76853405f78c48a2bc76c1ea5689cc66; _utm=ca54a19a243846f295be5534e68b377c; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522304%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjEyNDIxMCwiZXhwIjoxNTkzNjYwMjEwfQ.js_Alwxj9dx8j1CFpd_FYqwHsQ3Qzz9Umff6gDXiJcPZareY6TtFbtlFrNBK9xa9MzYPLHalemxlTXY_tbXDPQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjEyNDIxMCwiZXhwIjoxNTkzNjYwMjEwfQ.js_Alwxj9dx8j1CFpd_FYqwHsQ3Qzz9Umff6gDXiJcPZareY6TtFbtlFrNBK9xa9MzYPLHalemxlTXY_tbXDPQ; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1561540966,1562044107,1562123082,1562143132; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562222486'
    a      = 'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; jsid=SEM-BAIDU-PZ1907-SY-000000; _gid=GA1.2.343199843.1562553250; aliyungf_tc=AQAAAD3iO0l9lwAAvn4varh2ubXdBBOr; csrfToken=syR0e5uZ-4FlifUt0Si3QfIo; bannerFlag=undefined; _gat_gtag_UA_123487620_1=1; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562301042,1562310127,1562322914,1562636966; token=d5e7a0e2f70c42989c999ce9c0f33d12; _utm=33a8fa5b0e06477092ac1375084c724e; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522310%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjYzNjk5NSwiZXhwIjoxNTk0MTcyOTk1fQ.PFL3RyOFPcozaEUxNcQAuy3Fgtj-VTpCTjipFiEAEiOTMq1Y0irHs3AMry5HV2Jbuz90lDWs8YBfgazzlR5mWw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjYzNjk5NSwiZXhwIjoxNTk0MTcyOTk1fQ.PFL3RyOFPcozaEUxNcQAuy3Fgtj-VTpCTjipFiEAEiOTMq1Y0irHs3AMry5HV2Jbuz90lDWs8YBfgazzlR5mWw; RTYCID=5ee94e1f5d7d42aaba562cb1dad6494c; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562637005; CT_TYCID=f77962ec615c44088c1229c7cf09a56e; cloud_token=15746dda68924c5eadfb3f68cbcdbfd2; cloud_utm=49a44568fb114ac6829897b53bc6c426'
    cookie = 'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; jsid=SEM-BAIDU-PZ1907-SY-000000; _gid=GA1.2.343199843.1562553250; bannerFlag=undefined; RTYCID=5ee94e1f5d7d42aaba562cb1dad6494c; CT_TYCID=f77962ec615c44088c1229c7cf09a56e; aliyungf_tc=AQAAAC6WvkP02QIAvn4valNYLgdVEwp+; csrfToken=W_XaATj1qpm_R38WhH57T89X; token=4ee8a820c3754e91925aa612a6f5b0e9; _utm=a8c20f8e2bc3451e840201cd7eea7a0a; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562310127,1562322914,1562636966,1562644008; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522310%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjY0NDY5OCwiZXhwIjoxNTk0MTgwNjk4fQ.R4ymKt9IlymAakSRbEb3RgeO-vH7lrT9c6boyl4OKZ2M_Bj7rT1D1bCPmiwiF8wa0CrsFNOn2dZK6sDK-L7OoA%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjY0NDY5OCwiZXhwIjoxNTk0MTgwNjk4fQ.R4ymKt9IlymAakSRbEb3RgeO-vH7lrT9c6boyl4OKZ2M_Bj7rT1D1bCPmiwiF8wa0CrsFNOn2dZK6sDK-L7OoA; _gat_gtag_UA_123487620_1=1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562644700; cloud_token=ef0dd25430f34459abda4210c324839a; cloud_utm=2210ac2bed2042e28a681bf6196a194e; Hm_lvt_d5ceb643638c8ee5fbf79d207b00f07e=1562644726; Hm_lpvt_d5ceb643638c8ee5fbf79d207b00f07e=1562644726'
    cs = [cookie,a]
    cookies = {i.split("=")[0]:i.split("=")[1] for i in random.choice(cs).split("; ")}
    response = requests.get(url,headers=headers,cookies=cookies)
    if response.status_code == 200:
        return response
    else:

        return response.status_code



#解析响应内容
#参数为要查询的公司名
def parsed(keyword):
    response = getres(keyword)
    if isinstance(response,int):
        return response
    else:
        html =etree.HTML(response.text)
        gsname = ""
        gsname = html.xpath("string(//a[@class='name '])")
        if gsname:
            try:
                phone = eval(html.xpath('//div[@class="contact row "]/div[@class="col"][1]/script/text()')[0])
            except IndexError:
                phone = ""
            try:
                frname = html.xpath('//div[@class="title -wider text-ellipsis"]/a/@title')[0]
            except IndexError:
                frname = ""
            try:
                email = eval(html.xpath('//div[@class="contact row "]/div[@class="col"][2]/script/text()')[0])
            except IndexError:
                email = ""
            return {"gsname":gsname,"frname":frname,"phone":phone,"email":email}
        else:
            return ""
#写入数据库
def savefile(res):
    sql="""
        insert into skyeye(city,gsname,frname,phone,timestamp) values ('{}','{}','{}','{}','{}')
    """.format(res["gsname"][0:2],res["gsname"],res["frname"],";".join(res["phone"]),int(time.time()))
    try:
        curosr.execute(sql)
        db.commit()
    except:
        db.rollback()
def run(gslist="gongsi.txt",line=0):
    gongsi =[]
    with open(gslist,"r") as f:
        for i in f:
            gongsi.append(i)
        for ss in gongsi[line:]:
            res = parsed(ss)
            if isinstance(res,int):
                print(res)
                with open(gslist,"w") as fp:
                    for each in gongsi:
                        fp.write(each)
                break
            elif res != "":
                savefile(res)
                print("写入了:"+str(res))
                gongsi.remove(ss)
    curosr.close()
    db.close()


if __name__ == '__main__':
    run(gslist="100-150.txt",line=0)
    # print(getip.getip())
    # print(getres().text)