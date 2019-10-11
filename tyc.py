import requests
from fake_useragent import UserAgent
from lxml import etree
import chardet
import time
ua = UserAgent()

#获取响应
#参数为要查询的公司名
def getres(keyword,cookie):

    url ="https://www.tianyancha.com/search?key={}".format(keyword)

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
    # cookie = 'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; jsid=SEM-BAIDU-PZ1907-SY-000000; aliyungf_tc=AQAAAD3iO0l9lwAAvn4varh2ubXdBBOr; csrfToken=syR0e5uZ-4FlifUt0Si3QfIo; bannerFlag=undefined; _gid=GA1.2.1313374884.1562747826; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562644008,1562652285,1562747826,1562809283; token=3450b62648a0404ca545ebe8fedfa382; _utm=f444aaa0aa214e9a933253f16f14d4d3; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522312%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjgwOTMzMiwiZXhwIjoxNTk0MzQ1MzMyfQ.AdYI2pTQ4Ky8HL3gLwZqP0ui9VxlRjXJMb1iecax_I3Z6Asc2cik3_w9rFqf7LjFOzZRAnHR9Y-OoQnfHVT8KQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjgwOTMzMiwiZXhwIjoxNTk0MzQ1MzMyfQ.AdYI2pTQ4Ky8HL3gLwZqP0ui9VxlRjXJMb1iecax_I3Z6Asc2cik3_w9rFqf7LjFOzZRAnHR9Y-OoQnfHVT8KQ; cloud_token=b65854bbcdf24b97ad1b6f12478a26ab; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562810689; _gat_gtag_UA_123487620_1=1'
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
    response = requests.get(url,headers=headers,cookies=cookies)

    if response.status_code == 200:
        print("访问成功")
        return response
    else:
        print("访问失败,代码为{}".format(response.status_code))
        return response.status_code


#解析响应内容
#参数为要查询的公司名
def parsed(keyword,cookie):
    response = getres(keyword,cookie)
    # print(response)
    if isinstance(response,int):
        # print(response)
        return response
    else:
        html =etree.HTML(response.text)
        # print(response.text)
        gsname = html.xpath('string(//div[@class="search-item sv-search-company"]/div/div[3]/div[1]/a)')

        phone1 = html.xpath('//div[@class="search-item sv-search-company"][1]/div/div[3]/div[@class="contact row "]/div[1]/span/span[1]/text()')

        phone2 = html.xpath('//div[@class="search-item sv-search-company"][1]/div/div[3]/div[@class="contact row "]/div[1]/script/text()')
        if phone2 != []:
            phone = phone2[0]
        else:
            phone = phone1[0]
        frname = html.xpath('string(//div[@class="search-item sv-search-company"][1]/div/div[3]/div[@class="info row text-ellipsis"]/div/a)')
        print("解析成功")
        print(gsname,phone,frname)
        return {"gsname":gsname,"frname":frname,"phone":phone}
#写入数据库
def savefile(res):
    with open("查询结果.txt","a",encoding="utf-8") as f:
        f.write(res["gsname"]+" "+res["frname"]+" "+res["phone"]+"\n")
        # print("写入了:{}".format((res["gsname"]+" "+res["frname"]+" "+res["phone"]+"\n")))
def run(cookie='TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; jsid=SEM-BAIDU-PZ1907-SY-000000; aliyungf_tc=AQAAAD3iO0l9lwAAvn4varh2ubXdBBOr; csrfToken=syR0e5uZ-4FlifUt0Si3QfIo; bannerFlag=undefined; _gid=GA1.2.1313374884.1562747826; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562644008,1562652285,1562747826,1562809283; token=3450b62648a0404ca545ebe8fedfa382; _utm=f444aaa0aa214e9a933253f16f14d4d3; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522312%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjgwOTMzMiwiZXhwIjoxNTk0MzQ1MzMyfQ.AdYI2pTQ4Ky8HL3gLwZqP0ui9VxlRjXJMb1iecax_I3Z6Asc2cik3_w9rFqf7LjFOzZRAnHR9Y-OoQnfHVT8KQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU2MjgwOTMzMiwiZXhwIjoxNTk0MzQ1MzMyfQ.AdYI2pTQ4Ky8HL3gLwZqP0ui9VxlRjXJMb1iecax_I3Z6Asc2cik3_w9rFqf7LjFOzZRAnHR9Y-OoQnfHVT8KQ; cloud_token=b65854bbcdf24b97ad1b6f12478a26ab; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562810689; _gat_gtag_UA_123487620_1=1'):
    encoding=getencoding("公司名列表.txt")
    with open("公司名列表.txt","r",encoding=encoding) as fp:
        gslist = [i.strip() for i in fp]
    for gs in gslist:
        try:

            start=time.time()
            res = parsed(keyword=gs,cookie=cookie)
            if isinstance(res,int):
                print("请输入验证码后重新运行")
                exit()
            savefile(res)
            gslist.remove(gs)
            end=time.time()
            print("用时:",end-start)
        except:
            with open("公司名列表.txt","w",encoding=encoding) as fp:
                for s in gslist:
                    fp.write(s+"\n")
        finally:
            with open("公司名列表.txt","w",encoding=encoding) as fp:
                for s in gslist:
                    fp.write(s+"\n")

def getencoding(file):
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']
if __name__ == '__main__':
    # print(getencoding("公司名列表.txt"))
    cookie=input("请输入cookie:")
    if cookie =="":
        run()
    else:
        run(cookie)
    # parsed("北京皓智顺然")