import requests
from fake_useragent import UserAgent
from lxml import etree
import sendemail
import pymysql
import datetime
import random
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

    url ="https://www.tianyancha.com/search/ohp1/p{}?key={}".format(page,keyword)
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    print(url + " " +nowTime)
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
    cookie = 'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; jsid=SEM-BAIDU-PZ1907-SY-000100; aliyungf_tc=AQAAAJzZzjC3YQ0AUFcvaiFUeN88ecW0; csrfToken=OeP6IGPleNkdlXMDewo2KLqy; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1564650612,1565059597,1565084112,1565662831; _gid=GA1.2.1145345027.1565662832; RTYCID=5079377c890a44c6969c6337d4d07060; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25223%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522surday%2522%253A%2522350%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25221%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2NTc0NjQxMCwiZXhwIjoxNTk3MjgyNDEwfQ.Z_7Fy3inlXgZAMpB3RLZlyYK4VX57MT6IjrxdrRVPNfvTR4AkDhikluRj3JsI2lLArG3nnSaO3uyaF7kiiLD2w%2522%252C%2522vipToTime%2522%253A%25221595903278098%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522isExpired%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2NTc0NjQxMCwiZXhwIjoxNTk3MjgyNDEwfQ.Z_7Fy3inlXgZAMpB3RLZlyYK4VX57MT6IjrxdrRVPNfvTR4AkDhikluRj3JsI2lLArG3nnSaO3uyaF7kiiLD2w; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1565747085'
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
    try:
        response = requests.get(url,headers=headers,cookies=cookies)
    except Exception as e:
        print(str(e))
        response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code == 200:
        print("访问成功")
        return response
    else:
        while True:
            try:
                a=yanzheng(cookie,url)
                if a:
                    return 400
                # cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
                # chrome = webdriver.Chrome()
                # chrome.get("http://www.tianyancha.com")  # 先get一下后面才能加cookie
                # for i in cookies:
                #     chrome.add_cookie({"name": i, "value": cookies[i]})
                # chrome.get(url)
                # for i in cookies:
                #     chrome.add_cookie({"name": i, "value": cookies[i]})
                # time.sleep(20)
                # if chrome.current_url[:26] == "https://www.tianyancha.com":
                #     chrome.quit()
                #     return 400
            except:
                pass

def yanzheng(cookie,url):
    # ip = getip.getip()
    # val = '--proxy-server=http://' + ip
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument(val)
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
    print(res)
    if res == False:
        print(res[u'imgId'])
        client.report_err(res[u'imgId'])
        print("识别识别,已提交报错")
        return False
    else:
        print(res[u'result'])  # 识别结果
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
        return True
    else:
        # 当验证码识别错误时,报告错误
        print(res[u'imgId'])
        print(nowurl[:26])
        client.report_err(res[u'imgId'])
        print("识别识别,已提交报错")
        chrome.close()
        return False

def getpagenum(keyword):
    response = getres(keyword)
    # print(response.text)
    # exit()
    if isinstance(response, int):
        return None
    else:
        html = etree.HTML(response.text)
        resnum = html.xpath("//*[@id='search']/div[1]/span[2]/text()")[0]
        if resnum == "100000+":
            resnum=5000
        else:
            resnum=int(resnum)
        print("获取页数成功,页数为:{}".format(resnum))
        if resnum == 0:
            return 0
        elif resnum >5000:
            return 250
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
            phone1 = gs.xpath('string(.//div/span[2]/span)')#一个的号码
            phone2 = gs.xpath('.//div[1]/script/text()')#隐藏的多个号码
            email1 = gs.xpath('string(.//div[2]/span[2])')#邮箱
            email2 = gs.xpath('.//div[2]/script/text()')#隐藏的邮箱
            gsname = gs.xpath('string(.//../div[@class="header"]/a)')#公司名称
            frname = gs.xpath('string(.//../div[@class="info row text-ellipsis"]/div/a)')#法人名称
            city = gs.xpath('.//../../span[@class="site"]/text()')#城市
            if city != []:
                city = city[0]
            else:
                city = ""
            #成立日期
            buildtime =gs.xpath('.//../div[@class="info row text-ellipsis"]/div[3]/span/text()')

            #注册资本
            zczb = gs.xpath('.//../div[@class="info row text-ellipsis"]/div[2]/span/text()')

            #企业状态
            qyzt = gs.xpath('.//../div[@class="header"]/div/text()')
            #经营范围
            jyfw = gs.xpath('string(.//../div[@class="match row text-ellipsis"])')

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
            res = {"phone": phone, "gsname": gsname, "frname": frname, "city": city, "email": email,"zczb":zczb[0] if zczb != [] else "","buildtime":buildtime[0] if buildtime!= [] else "","qyzt":qyzt[0] if qyzt != [] else "","jyfw":jyfw}
            # print(res)
            if phone != "":
                result.append(res)
        print("解析成功")
        print(result)
        return result
#写入数据库
def savefile(res):
    sql = """
            insert into tyclist(city,gsname,frname,phone,email,zczb,qyzt,buildtime,jyfw) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(res["city"], res["gsname"], res["frname"], res["phone"], res["email"],res["zczb"],res["qyzt"],res["buildtime"],res["jyfw"])
    try:
        curosr.execute(sql)
        db.commit()
        print("写入了:{},{},{},{},{}".format(res["city"], res["gsname"], res["frname"], res["phone"], res["email"]))
    except:
        db.rollback()
        print("发生错误，回滚事务")
def run(num,keyword):
    keylist =keymath()
    citylist=[]

    with open("gongsi2.txt","r") as f:
        for l in f:
            citylist.append(l[0:-1])
        # print(citylist)
        # exit()
    for key in keylist:
        pagenum = getpagenum(key)
        if pagenum != None:
            for page in range(num if key == keyword else 1,pagenum+1):
                ress = parsed(key,page)
                if ress == 400:
                    with open("gongsi2.txt","w") as fp:
                        for ss in citylist:
                            fp.write(ss+"\n")
                    continue
                print("当前page是"+str(page))
                print("查询关键词:{}".format(key))

                for res in ress:
                    # pass
                    savefile(res)
                # s= random.randint(1,3)
                time.sleep(3)
                print("第{}页抓取完成，休息{}秒".format(page,3))
            city=key.replace("消防工程","")
            # print(city)
            citylist.remove(city)
        else:
            print("没获取到页数")
        # print(citylist)
        # exit()


def keymath():

    # keylist = ["建筑", "劳务", "建筑劳务", "建筑工程", "消防工程", "监理", "工程建设", "工程建筑", '工程','消防安全工程']
    keylist=["消防工程"]
    keyword_list =[]
    citylist = []
    with open("gongsi2.txt","r") as f:
        for line in f:
            citylist.append(line[0:-1])
        for key in keylist:
            for line in citylist:
                keyword_list.append(line+key)
        return keyword_list

if __name__ == '__main__':
    # time.sleep(20000)
    # exit()

    try:
        run(118,"乌鲁木齐市消防工程")
    except IndexError as e:
        print(str(e))
        sendemail.sendemail("li.yansong@hzsr-media.com","程序停止啦","错误信息是:"+str(e))
        exit()
    except Exception as f:
        print(str(f))
    # print(parsed("岳阳市建筑劳务",1))
