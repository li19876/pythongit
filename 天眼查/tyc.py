import time
import tools
import chardet
import easygui as e
import requests
import random
from urllib.parse import quote
import os
from fake_useragent import UserAgent
from lxml import etree
ua = UserAgent()


# 获取响应
# 参数为要查询的公司名
def getres(keyword, cookie):
    timestamp = time.time()
    randomstr = random.randint(10000000, 99999999)
    sign = str(timestamp) + '.' + str(randomstr)
    url = "https://www.tianyancha.com/search?key={}".format(keyword)

    header = """authority: www.tianyancha.com
method: GET
path: /search?key={}
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
referer: https://www.tianyancha.com/search?key={}&sessionNo={}
sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: {}""".format(quote(keyword),quote(keyword),sign,ua.random)
    headers= tools.make_header(header)
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        print("访问成功")
        
        return response
    else:
        print("访问失败,代码为{}".format(response.status_code))
        return response.status_code


# 解析响应内容
# 参数为要查询的公司名

def parsed(keyword, cookie):
    response = getres(keyword, cookie)
    print("查询公司名:"+keyword)
    # print(response)
    if isinstance(response, int):
        # print(response)
        return response
    else:
        html = etree.HTML(response.text)
        
        gsname = html.xpath('string(//a[@class="index_alink__zcia5 link-click"][1]/span)')
        
        phone = html.xpath('string(//span[@class="index_link-hover__Do0lM"][1])')
        print("电话:",phone)
        frname = html.xpath(
            'string(//div[@class="index_info-col__UVcZb index_wider__gQok0"][1]/a)')
        if gsname == "" and frname == "" and phone == "":
            with open('test.html', 'w', encoding='utf-8') as f:
                f.write(keyword)
                f.write(response.text)
            if(response.text[0:15] == '<html><script>'):
                return 400
            else:
                return 0
        print("解析成功")
        print("查询结果是:",gsname, phone, frname)
        
        return {"gsname": gsname, "frname": frname, "phone": phone}


# 写入数据库
def savefile(res,gslist):
    with open("查询结果.txt", "a", encoding="utf-8") as f:
        f.write(res["gsname"] + " " + res["frname"] + " " + res["phone"] + "\n")
        print("写入了:{}".format((res["gsname"]+" "+res["frname"]+" "+res["phone"]+"\n")))
    encoding = getencoding("公司名列表.txt")
    with open("公司名列表.txt", "w", encoding=encoding) as fp:
        for s in gslist:
            fp.write(s + "\n")


def run(cookie):
    encoding = getencoding("公司名列表.txt")
    with open("公司名列表.txt", "r", encoding=encoding) as fp:
        gslist = [i.strip() for i in fp]
    print(gslist)
    flag = 0
    while len(gslist)>0:
        # try:
        gs = gslist.pop(0)
        start = time.time()
        res = parsed(keyword=gs, cookie=cookie)
        if isinstance(res, int):
            if(res == 400):
                boo=e.boolbox("出错了，继续查询点击yes")
                if boo:
                    continue
            else:
                if flag<= 3:
                    flag += 1
                    print("获取内容失败")
                    time.sleep(1)
                else:
                    print('失败三次，停止')
                    break
        else:
            flag = 0
            savefile(res,gslist)
            end = time.time()
            print("用时:", end - start)
            time.sleep(1)
        # except Exception as e:
        #     print(e)
        #     with open("公司名列表.txt", "w", encoding=encoding) as fp:
        #         for s in gslist:
        #             fp.write(s + "\n")
        # finally:
        #     with open("公司名列表.txt", "w", encoding=encoding) as fp:
        #         for s in gslist:
        #             fp.write(s + "\n")


def getencoding(file):
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print(getencoding("公司名列表.txt"))
    with open("./cook.txt",'r',encoding=getencoding("cook.txt")) as f:
        cookie = f.read()
    if cookie == "":
        e.msgbox("请输入cookie后运行!")
    else:
        run(cookie)
    # parsed("北京皓智顺然")
    # a = e.boolbox("是否验证完成?")
    # print(a)