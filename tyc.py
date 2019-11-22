import time

import chardet
import easygui as e
import requests
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()


# 获取响应
# 参数为要查询的公司名
def getres(keyword, cookie):
    url = "https://www.tianyancha.com/search?key={}".format(keyword)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.tianyancha.com',
        'Referer': 'https://www.tianyancha.com/search?key=%E5%A4%A9%E6%B4%A5%E6%95%99%E8%82%B2',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua.random
    }
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
        # print(response.text)
        gsname = html.xpath('string(//div[@class="search-item sv-search-company"]/div/div[3]/div[1]/a)')

        phone1 = html.xpath('//div[@class="search-item sv-search-company"][1]/div/div[3]/div[@class="contact row '
                            '"]/div[1]/span/span[1]/text()')

        phone2 = html.xpath('//div[@class="search-item sv-search-company"][1]/div/div[3]/div[@class="contact row '
                            '"]/div[1]/script/text()')
        if phone2:
            phone = phone2[0]
        else:
            phone = phone1[0]
        frname = html.xpath(
            'string(//div[@class="search-item sv-search-company"][1]/div/div[3]/div[@class="info row '
            'text-ellipsis"]/div/a)')
        print("解析成功")
        print("查询结果是:",gsname, phone, frname)
        return {"gsname": gsname, "frname": frname, "phone": phone}


# 写入数据库
def savefile(res):
    with open("查询结果.txt", "a", encoding="utf-8") as f:
        f.write(res["gsname"] + " " + res["frname"] + " " + res["phone"] + "\n")
        # print("写入了:{}".format((res["gsname"]+" "+res["frname"]+" "+res["phone"]+"\n")))


def run(cookie):
    encoding = getencoding("公司名列表.txt")
    with open("公司名列表.txt", "r", encoding=encoding) as fp:
        gslist = [i.strip() for i in fp]
    print(gslist)
    while len(gslist)>0:
        try:
            gs = gslist.pop(0)
            start = time.time()
            res = parsed(keyword=gs, cookie=cookie)
            if isinstance(res, int):
                while True:
                    boo=e.boolbox("请到天眼查输入验证码,验证完成后点击yes!")
                    if boo:
                        break
            savefile(res)
            end = time.time()
            print("用时:", end - start)
        except:
            with open("公司名列表.txt", "w", encoding=encoding) as fp:
                for s in gslist:
                    fp.write(s + "\n")
        finally:
            with open("公司名列表.txt", "w", encoding=encoding) as fp:
                for s in gslist:
                    fp.write(s + "\n")


def getencoding(file):
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']


if __name__ == '__main__':
    # print(getencoding("公司名列表.txt"))
    with open("./cook.txt",'r',encoding=getencoding("cook.txt")) as f:
        cookie = f.read()
    if cookie == "":
        e.msgbox("请输入cookie后运行!")
    else:
        run(cookie)
    # parsed("北京皓智顺然")
    # a = e.boolbox("是否验证完成?")
    # print(a)
