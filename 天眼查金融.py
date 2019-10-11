import requests
from fake_useragent import UserAgent
from lxml import etree
import easygui as e
import csv
import time
import pymysql
ua = UserAgent()
db =pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
curosr = db.cursor()


#获取响应
#参数为要查询的公司名
def getres(keyword= "北京皓智顺然",page=1):

    url ="https://www.tianyancha.com/search/p{}?key={}".format(page,keyword)

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'www.tianyancha.com',
        'Referer':'https://www.tianyancha.com/vipintro/?jsid=SEM-BAIDU-PZ1907-SY-000000',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':ua.random
    }
    #c     = 'jsid=SEM-BAIDU-PP-VI-000873; TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; aliyungf_tc=AQAAAIHF7VU/tAMAvn4vajbCkcsjt5Kh; bannerFlag=undefined; csrfToken=CjTQs6nrjHmjMUNT0kPY8eLU; _gid=GA1.2.656427539.1562044105; token=76853405f78c48a2bc76c1ea5689cc66; _utm=ca54a19a243846f295be5534e68b377c; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522304%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjEyNDIxMCwiZXhwIjoxNTkzNjYwMjEwfQ.js_Alwxj9dx8j1CFpd_FYqwHsQ3Qzz9Umff6gDXiJcPZareY6TtFbtlFrNBK9xa9MzYPLHalemxlTXY_tbXDPQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjEyNDIxMCwiZXhwIjoxNTkzNjYwMjEwfQ.js_Alwxj9dx8j1CFpd_FYqwHsQ3Qzz9Umff6gDXiJcPZareY6TtFbtlFrNBK9xa9MzYPLHalemxlTXY_tbXDPQ; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1561540966,1562044107,1562123082,1562143132; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562222486'
    cookie = 'aliyungf_tc=AQAAANTwcBNY3goA9lIvauHdBh4B27Da; csrfToken=sw0ow6YC6dEVksmjPLKfuDSb; jsid=SEM-BAIDU-PZ1907-SY-000000; TYCID=7a578c30a6da11e994d64573e5946644; undefined=7a578c30a6da11e994d64573e5946644; ssuid=9740429390; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1563179288; _ga=GA1.2.1498108650.1563179288; _gid=GA1.2.1615858823.1563179288; token=74a534ba6e5148628a5041fba9c77269; _utm=9499f59b608e49158c350fcb34390d5f; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25221%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25BC%25A0%25E9%2583%2583%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTY5OTUzNTIwNyIsImlhdCI6MTU2MzE3OTY4NiwiZXhwIjoxNTk0NzE1Njg2fQ.1zJuKOYQK8D-2QYHb9iLAkH1t8CFBrrGwldR-kqnLMNAh070q3h9kd43Hsr3UeEHPCW5X7jMiY3yFD0ikDROaA%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215699535207%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTY5OTUzNTIwNyIsImlhdCI6MTU2MzE3OTY4NiwiZXhwIjoxNTk0NzE1Njg2fQ.1zJuKOYQK8D-2QYHb9iLAkH1t8CFBrrGwldR-kqnLMNAh070q3h9kd43Hsr3UeEHPCW5X7jMiY3yFD0ikDROaA; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1563179688'
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
    response = requests.get(url,headers=headers,cookies=cookies)

    if response.status_code == 200:
        print("访问成功")
        return response
    else:
        print("访问失败,代码为{}".format(response.status_code))
        return response.status_code

def getpagenum(keyword):
    response = getres(keyword)
    if isinstance(response, int):
        return response
    else:
        html = etree.HTML(response.text)
        resnum = html.xpath("//*[@id='search']/div[1]/span[2]/text()")[0]
        if resnum == "100000+":
            resnum=100000
        else:
            resnum=int(resnum)
        print("获取页数成功,页数为:{}".format(resnum))
        if resnum == 0:
            return 0
        elif resnum >100:
            return 5
        else:
            return resnum//20+1

#解析响应内容
#参数为要查询的公司名
def parsed(keyword,page):
    response = getres(keyword,page)
    if isinstance(response,int):
        return response
    else:
        html =etree.HTML(response.text)
        lxlist = html.xpath('//div[@class="contact row "]')
        # print(lxlist)
        # print(response.text)
        result = []
        for gs in lxlist:
            phone1 = gs.xpath('string(.//div/span[2]/span)')
            phone2 = gs.xpath('.//div[1]/script[1]/text()')
            gsname = gs.xpath('string(.//../div[@class="header"]/a)')
            frname = gs.xpath('string(.//../div[@class="info row text-ellipsis"]/div/a)')
            city   = gs.xpath('.//../../span[@class="site"]/text()')
            if city !=[]:
                city =city[0]
            else:
                city =""
            # print(phone2)
            if phone2 != []:
                phone = eval(phone2[0])
                listphone = list(filter(lambda a: len(a) == 11, phone))
                phone = ",".join(listphone)
            elif len(phone1) == 11:
                phone = phone1
            else:
                phone = ""
            res = {"phone":phone,"gsname":gsname,"frname":frname,"city":city}
            if phone != "":
                result.append(res)
        print("解析成功")
        # print(result)
        return result
#写入数据库
def savefile(res):
    sql="""
        insert into tycjr(city,gsname,frname,phone) values ('{}','{}','{}','{}')
    """.format(res["city"],res["gsname"],res["frname"],res["phone"])
    try:
        curosr.execute(sql)
        db.commit()
        print("写入了:{},{},{},{}".format(res["city"],res["gsname"],res["frname"],(res["phone"])))
    except:
        db.rollback()
def run():
    keylist =keymath()
    citylist=[]
    with open("gongsi3.txt","r") as f:
        for l in f:
            citylist.append(l[0:-1])
        # print(citylist)
        # exit()
    for key in keylist:
        pagenum = getpagenum(key)
        for page in range(1,pagenum+1):
            ress = parsed(key,page)
            if ress == 400:
                with open("gongsi3.txt","w") as fp:
                    for ss in citylist:
                        fp.write(ss+"\n")
                e.msgbox("360隐身该写验证码了,目前的关键词是:"+key)
                exit()
            print("查询关键词:{}".format(key))
            for res in ress:
                # pass
                savefile(res)
            print("一页完成,休息半秒")
        city=key.replace("金融机构","")
        # print(city)
        citylist.remove(city)
        # print(citylist)
        # exit()
        time.sleep(0.5)






def keymath():

    # keylist = ["建筑", "劳务", "建筑劳务", "建筑工程", "消防工程", "监理", "工程建设", "工程建筑", '工程']
    keylist=["金融机构"]
    keyword_list =[]
    citylist = []
    with open("gongsi3.txt","r") as f:
        for line in f:
            citylist.append(line[0:-1])
        for key in keylist:
            for line in citylist:
                keyword_list.append(line+key)
        return keyword_list

if __name__ == '__main__':
    run()
    # print(parsed("岳阳市建筑劳务",1))