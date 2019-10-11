import requests
from fake_useragent import UserAgent
from lxml import etree
import easygui as e
import pymysql
import getip
import time
import main
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
        'Referer':'https://www.tianyancha.com/vipintro/?jsid=SEM-BAIDU-PZ1907-SY-000000&rnd=',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':ua.random
    }
    #c     = 'jsid=SEM-BAIDU-PP-VI-000873; TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; aliyungf_tc=AQAAAIHF7VU/tAMAvn4vajbCkcsjt5Kh; bannerFlag=undefined; csrfToken=CjTQs6nrjHmjMUNT0kPY8eLU; _gid=GA1.2.656427539.1562044105; token=76853405f78c48a2bc76c1ea5689cc66; _utm=ca54a19a243846f295be5534e68b377c; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522304%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjEyNDIxMCwiZXhwIjoxNTkzNjYwMjEwfQ.js_Alwxj9dx8j1CFpd_FYqwHsQ3Qzz9Umff6gDXiJcPZareY6TtFbtlFrNBK9xa9MzYPLHalemxlTXY_tbXDPQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjEyNDIxMCwiZXhwIjoxNTkzNjYwMjEwfQ.js_Alwxj9dx8j1CFpd_FYqwHsQ3Qzz9Umff6gDXiJcPZareY6TtFbtlFrNBK9xa9MzYPLHalemxlTXY_tbXDPQ; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1561540966,1562044107,1562123082,1562143132; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562222486'
    cookie =  'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; aliyungf_tc=AQAAAD3iO0l9lwAAvn4varh2ubXdBBOr; csrfToken=syR0e5uZ-4FlifUt0Si3QfIo; bannerFlag=undefined; cloud_token=32a6985c94ad4c4ca85b6fdc080446f7; _gid=GA1.2.1855709371.1563762847; token=44a7e22a158745af812a6a371ec6e639; _utm=f9d7344984fb49bf931badb0e12b0dd8; jsid=SEM-BAIDU-PZ1907-SY-000100; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522320%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2Mzc2Mjg2OSwiZXhwIjoxNTk1Mjk4ODY5fQ.K2Z58G3uh0i-WM0zduS5-nP-LKw_3H33YC1vyEHtxV_yEexq1mGLylgAittUaEdKxUONQAxbiKnewPoVfAMr_w%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2Mzc2Mjg2OSwiZXhwIjoxNTk1Mjk4ODY5fQ.K2Z58G3uh0i-WM0zduS5-nP-LKw_3H33YC1vyEHtxV_yEexq1mGLylgAittUaEdKxUONQAxbiKnewPoVfAMr_w; _gat_gtag_UA_123487620_1=1; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562747826,1562809283,1563775797,1563776937; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1563776943'
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
    response = requests.get(url,headers=headers,cookies=cookies)

    if response.status_code == 200:
        print("访问成功")
        return response
    else:
        # cookie = 'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; jsid=SEM-BAIDU-PZ1907-SY-000000; aliyungf_tc=AQAAAD3iO0l9lwAAvn4varh2ubXdBBOr; csrfToken=syR0e5uZ-4FlifUt0Si3QfIo; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562644008,1562652285,1562747826,1562809283; cloud_token=32a6985c94ad4c4ca85b6fdc080446f7; _gid=GA1.2.1855709371.1563762847; _gat_gtag_UA_123487620_1=1; token=44a7e22a158745af812a6a371ec6e639; _utm=f9d7344984fb49bf931badb0e12b0dd8; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522320%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2Mzc2Mjg2OSwiZXhwIjoxNTk1Mjk4ODY5fQ.K2Z58G3uh0i-WM0zduS5-nP-LKw_3H33YC1vyEHtxV_yEexq1mGLylgAittUaEdKxUONQAxbiKnewPoVfAMr_w%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2Mzc2Mjg2OSwiZXhwIjoxNTk1Mjk4ODY5fQ.K2Z58G3uh0i-WM0zduS5-nP-LKw_3H33YC1vyEHtxV_yEexq1mGLylgAittUaEdKxUONQAxbiKnewPoVfAMr_w; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1563762878'
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
        chrome = webdriver.Chrome()
        chrome.set_window_size(500, 500)
        chrome.get("http://www.tianyancha.com")  # 先get一下后面才能加cookie
        for i in cookies:
            chrome.add_cookie({"name": i, "value": cookies[i]})
        chrome.get(url)
        for i in cookies:
            chrome.add_cookie({"name": i, "value": cookies[i]})
        ele = chrome.find_element_by_class_name("new-box94")  # 获取到验证码div
        ele.screenshot("img.png")  # 截图
        actions = ActionChains(chrome)
        client = main.Chaoren()
        client.data['username'] = 'li1462063555'  # 修改为打码账号
        client.data['password'] = '19980706..'  # 修改为打码密码
        # 查剩余验证码点数
        print(client.get_left_point())

        # 提交识别
        imgdata = open('img.png', 'rb').read()
        res = client.recv_byte(imgdata)
        print(res[u'result'])  # 识别结果
        if res[u'result'] == False:
            print(res[u'imgId'])
            client.report_err(res[u'imgId'])
            print("识别识别,已提交报错")
            return None
        zb = res[u'result'].split(";")[0:-1]
        print("坐标是{}".format(zb))
        for z in zb:
            actions.move_to_element_with_offset(ele, int(z.split(",")[0]), int(z.split(",")[1])).click().perform()
            print("点击了{}".format(z.split(",")[0] + "," + z.split(",")[1]))
        tijiao = chrome.find_element_by_id("submitie")
        actions.move_to_element_with_offset(tijiao, 60, 15).click().perform()
        time.sleep(5)
        nowurl = chrome.current_url
        if nowurl[:26] == "https://www.tianyancha.com":
            print("识别成功")
            print(nowurl[:26])
            chrome.close()
        else:
            # 当验证码识别错误时,报告错误
            print(res[u'imgId'])
            print(nowurl[:26])
            client.report_err(res[u'imgId'])
            print("识别识别,已提交报错")
            chrome.close()
        # print("访问失败,代码为{}".format(response.status_code))
        return 400

def getpagenum(keyword):
    response = getres(keyword)
    if isinstance(response, int):
        return None
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
            phone2 = gs.xpath('.//div[1]/script/text()')
            email1 = gs.xpath('string(.//div[2]/span[2])')
            email2 = gs.xpath('.//div[2]/script/text()')
            gsname = gs.xpath('string(.//../div[@class="header"]/a)')
            frname = gs.xpath('string(.//../div[@class="info row text-ellipsis"]/div/a)')
            city = gs.xpath('.//../../span[@class="site"]/text()')
            if city != []:
                city = city[0]
            else:
                city = ""
            # print(phone2)
            if phone2 != []:
                phone = eval(phone2[0])
                listphone = list(filter(lambda a: len(a) == 11, phone))
                phone = ",".join(listphone)
            elif len(phone1) == 11:
                phone = phone1
            else:
                phone = ""
            if email2 != []:
                email = email2[0].replace("[", "").replace("]", "").replace('"', "")
            else:
                email = email1
            res = {"phone": phone, "gsname": gsname, "frname": frname, "city": city, "email": email}
            if phone != "":
                result.append(res)
        print("解析成功")
        # print(result)
        return result
#写入数据库
def savefile(res):
    sql = """
            insert into tyclist2(city,gsname,frname,phone,email) values ('{}','{}','{}','{}','{}')
        """.format(res["city"], res["gsname"], res["frname"], res["phone"], res["email"])
    try:
        curosr.execute(sql)
        db.commit()
        print("写入了:{},{},{},{},{}".format(res["city"], res["gsname"], res["frname"], res["phone"], res["email"]))
    except:
        db.rollback()
def run():
    keylist =keymath()
    citylist=[]
    with open("gongsi.txt","r") as f:
        for l in f:
            citylist.append(l[0:-1])
        # print(citylist)
        # exit()
    for key in keylist:
        pagenum = getpagenum(key)
        if pagenum != None:
            for page in range(1,pagenum+1):
                ress = parsed(key,page)
                if ress == 400:
                    with open("gongsi.txt","w") as fp:
                        for ss in citylist:
                            fp.write(ss+"\n")
                    continue
                print("查询关键词:{}".format(key))
                for res in ress:
                    # pass
                    savefile(res)
            city=key.replace("建筑施工","")
            # print(city)
            citylist.remove(city)
        else:
            print("没获取到页数")
        # print(citylist)
        # exit()







def keymath():

    # keylist = ["建筑", "劳务", "建筑劳务", "建筑工程", "消防工程", "监理", "工程建设", "工程建筑", '工程']
    keylist=["建筑施工"]
    keyword_list =[]
    citylist = []
    with open("gongsi.txt","r") as f:
        for line in f:
            citylist.append(line[0:-1])
        for key in keylist:
            for line in citylist:
                keyword_list.append(line+key)
        return keyword_list

if __name__ == '__main__':
    # time.sleep(20000)
    # exit()
    run()
    # print(parsed("岳阳市建筑劳务",1))