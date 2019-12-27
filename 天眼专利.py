import time
from lxml import etree
import requests
import datetime
import re
import os
import sys
def get(keyword,page):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'zhuanli.tianyancha.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    url ='https://zhuanli.tianyancha.com/search/{}/p{}'.format(keyword,page)
    cookie='TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; __insp_wid=677961980; __insp_slim=1565856225188; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY2xhaW0vYXBwbHkvMzM2MTM4MTQyMT9wcmljaW5nUGFja2FnZT0wJmVkaXRNb2JpbGU9MQ%3D%3D; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; _gid=GA1.2.272920010.1577427146; RTYCID=bb1b80f2d3fc41a3af52f375f9236a33; CT_TYCID=9b039d9169624b44a8cacf71d5703964; cloud_token=a53846ad75b8432086543b92ec8b9066; bannerFlag=true; jsid=SEM-BAIDU-PP-VI-000873; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1574995359,1575967374,1577427146,1577437386; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1577437386; aliyungf_tc=AQAAAGDhYCurPg8ArXwvamp0dppw7TVK; csrfToken=caR0Drm9aUSN0CKu06h951Xt; Hm_lvt_1c93ed18b9ecc941567e9f8a07cb6a61=1577437437; token=c74196c4a8924078b3ffe145fa3fa89c; _utm=519c2595dbd743a8b50a28c1cf59923d; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzc1Njc5OTI1MCIsImlhdCI6MTU3NzQzODQ4MiwiZXhwIjoxNTkyOTkwNDgyfQ.5DKlVd9x1wK4OqmqmeKe3Pq6rthtMygZDsg9gQ_n_NNJ-qGEqMvAb4VkE8pmzLyR49aOSMxVYNWrEvnQqpVMzg%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25221%2522%252C%2522nickname%2522%253A%2522%25E7%25BD%2597%25E6%259E%2597%25C2%25B7%25E5%25B8%2583%25E5%2585%25B0%25E8%2580%2583%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213756799250%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzc1Njc5OTI1MCIsImlhdCI6MTU3NzQzODQ4MiwiZXhwIjoxNTkyOTkwNDgyfQ.5DKlVd9x1wK4OqmqmeKe3Pq6rthtMygZDsg9gQ_n_NNJ-qGEqMvAb4VkE8pmzLyR49aOSMxVYNWrEvnQqpVMzg; Hm_lpvt_1c93ed18b9ecc941567e9f8a07cb6a61=1577438726'
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
    res=requests.get(url,headers=headers,cookies=cookies)
    return res.text

def get_detail(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'zhuanli.tianyancha.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    cookie = 'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; __insp_wid=677961980; __insp_slim=1565856225188; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY2xhaW0vYXBwbHkvMzM2MTM4MTQyMT9wcmljaW5nUGFja2FnZT0wJmVkaXRNb2JpbGU9MQ%3D%3D; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; _gid=GA1.2.272920010.1577427146; RTYCID=bb1b80f2d3fc41a3af52f375f9236a33; CT_TYCID=9b039d9169624b44a8cacf71d5703964; cloud_token=a53846ad75b8432086543b92ec8b9066; bannerFlag=true; jsid=SEM-BAIDU-PP-VI-000873; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1574995359,1575967374,1577427146,1577437386; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1577437386; aliyungf_tc=AQAAAGDhYCurPg8ArXwvamp0dppw7TVK; csrfToken=caR0Drm9aUSN0CKu06h951Xt; Hm_lvt_1c93ed18b9ecc941567e9f8a07cb6a61=1577437437; token=c74196c4a8924078b3ffe145fa3fa89c; _utm=519c2595dbd743a8b50a28c1cf59923d; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzc1Njc5OTI1MCIsImlhdCI6MTU3NzQzODQ4MiwiZXhwIjoxNTkyOTkwNDgyfQ.5DKlVd9x1wK4OqmqmeKe3Pq6rthtMygZDsg9gQ_n_NNJ-qGEqMvAb4VkE8pmzLyR49aOSMxVYNWrEvnQqpVMzg%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25221%2522%252C%2522nickname%2522%253A%2522%25E7%25BD%2597%25E6%259E%2597%25C2%25B7%25E5%25B8%2583%25E5%2585%25B0%25E8%2580%2583%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213756799250%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzc1Njc5OTI1MCIsImlhdCI6MTU3NzQzODQ4MiwiZXhwIjoxNTkyOTkwNDgyfQ.5DKlVd9x1wK4OqmqmeKe3Pq6rthtMygZDsg9gQ_n_NNJ-qGEqMvAb4VkE8pmzLyR49aOSMxVYNWrEvnQqpVMzg; Hm_lpvt_1c93ed18b9ecc941567e9f8a07cb6a61=1577438726'
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
    res = requests.get(url, headers=headers, cookies=cookies)
    if res.status_code == 200:
        return res.text
    return res.status_code

if __name__=='__main__':
    keyword='阿里巴巴'
    # one=get(keyword,'1')
    # html=etree.HTML(one)
    # zongnum = html.xpath('//*[@id="search"]/div[1]/div/div/span/text()')
    # page =250 if zongnum[0]=="5000+" else zongnum // 20 + 1
    # for i in range(1,page+1):
    #     res = get(keyword,i)
    #     html = etree.HTML(res)
    #     reslist = html.xpath('//div[@class="header"]/a/@href')
    #     with open(keyword+'url.txt','a') as f:
    #         for s in reslist:
    #             f.write(s)
    #     print('一页完成,休息1s')
    #     time.sleep(1)
    urllist=[]

    with open("阿里巴巴url.txt",'r') as f:
        isExists = os.path.exists(keyword)
        if not isExists:
            os.mkdir(keyword)
        else:
            pass
        for i in f:
            urllist.append(i)
    for s in urllist:
        res =get_detail(s.strip())
        if not isinstance(res,int):
            with open(keyword+os.sep+str(urllist.index(s))+'.html','w',encoding='utf-8') as p:
                p.write(res)
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'爬取成功:',str(urllist.index(s))+'.html')
        else:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'爬取失败,状态码是:',res)
        # time.sleep(1)




