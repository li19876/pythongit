# coding=utf-8
"""
Author:song
"""
import json
import sys

import re

import requests
import tools
def run(longurl):
    url = 'https://api.weibo.com/webim/2/direct_messages/new.json'
    headers = tools.make_header("""Accept: application/json, text/plain, */*
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Length: 199
    Content-Type: application/x-www-form-urlencoded
    Host: api.weibo.com
    Origin: https://api.weibo.com
    Pragma: no-cache
    Referer: https://api.weibo.com/chat/
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36""")
    cookies = tools.make_cookie("""SINAGLOBAL=5764344598274.942.1563766681306; UM_distinctid=170a95ab149859-01d4d4ede31937-43450521-1aeaa0-170a95ab14a68e; login_sid_t=9b16e1152ed2b84cc47b7ce9b3f53be2; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWfuMjX-sCx3smP.qsFZolD5JpX5K2hUgL.Fo-NSoB4e05f1K22dJLoIE-LxKqL1hnL1K8ki--fiK.RiKL8i--Xi-zRi-8Wi--ciK.0i-2c; ALF=1625881169; SSOLoginState=1594345172; SCF=AoDXATS15-GEbwppbXdaPhpnzovk0AOEJictIRg1fAixu3epNSORHt23NHZZcjMbH-UUg9jpNkBaVASeVFrcDXI.; SUB=_2A25yA7aEDeRhGeNJ7VYY8y7Jwj2IHXVReK9MrDV8PUNbmtANLW7mkW9NS6dfmYDGaAoIXGvETq-xPP0WdGbBFIBG; SUHB=0k1CYCKolcGpPs; un=18202610240; Apache=5706547280402.554.1594345170301; ULV=1594345170305:17:2:1:5706547280402.554.1594345170301:1593567061575; wvr=6; CNZZDATA1272960323=258231521-1588148282-https%253A%252F%252Fweibo.com%252F%7C1594341863; webim_unReadCount=%7B%22time%22%3A1594345772783%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; JSESSIONID=DB8CCFCF6050D83D814DFDA572EA83E2; UOR=www.tx022.com,widget.weibo.com,www.douban.com""")
    data = tools.make_header("""text: https://api.weibo.com/chat/#/chat?source_from=2
uid: 2028810631
extensions: {"clientid":"toiy1au2hnjdhkmxz8cwte1v2vdiy"}
is_encoded: 0
decodetime: 1
source: 209678993""")
    data['text']=longurl
    res = requests.post(url,headers=headers,cookies=cookies,data=data)
    # print(res.text)
    ss = re.findall(r'url_short":"(.+?)"', res.text)
    print(ss[0])

if __name__ == '__main__':
    # url=sys.argv[1]
    url = 'https://member.pizzahut.com.cn/service/app/usercenter/coupon.do?selectIndex=2&utm_source=wechat_menu_SuWan'
    run(url)


    # print(ss)
    # print(json_data)
    # print(json.loads(json_data))

