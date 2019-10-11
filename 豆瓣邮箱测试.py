import requests
from fake_useragent import UserAgent
import time
import random
ua= UserAgent()
# url = "https://accounts.douban.com/j/mobile/reset_password/request_email_code"
url = "http://httpbin.org/ip/"
ip =['123.55.3.45:46820',
'117.63.206.187:37400',
'221.227.169.59:25515',
'111.76.137.14:28849',
'171.80.155.94:35947',
'1.195.11.123:36847',
'49.76.198.165:20410',
'49.69.61.207:38048',
'106.58.115.136:24702',
'121.9.199.130:48908']
headers ={'User-Agent':ua.random,
          'referer':'https://accounts.douban.com/passport/get_password',
          'Accept':'application/json',
          'Accept-Encoding':'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9',
          'Connection': 'keep-alive',
          'Content-Length': '29',
          'Content-Type': 'application/x-www-form-urlencoded',
          'Host': 'accounts.douban.com',
          'Origin': 'https://accounts.douban.com'

}
with open("email.txt","r") as f:
    for s in range(1000000):
        em=f.readline()
        data={"ck":"","email":em}
        cookie = 'bid=LukZleEM_00; douban-fav-remind=1; UM_distinctid=16b9843b423259-003ae0662e53c5-43450521-15f900-16b9843b4243c3; ll="108289"; __utma=30149280.1570587171.1561627703.1561627703.1562232062.2; __utmc=30149280; __utmz=30149280.1562232062.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=30149280.2.10.1562232062; CNZZDATA1272964020=1464017346-1562231765-https%253A%252F%252Faccounts.douban.com%252F%7C1562231765'
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
        res =requests.post(url,headers=headers,data=data,proxies={"http":random.choice(ip)})
        print(res.text)
        time.sleep(0.5)
