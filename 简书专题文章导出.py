import requests
import json
import time
from lxml import etree
import csv
from fake_useragent import UserAgent
ua= UserAgent()
for i in range(2,3):
    url = "https://www.jianshu.com/c/a480500350e7?order_by=added_at&page="+str(i)
    header ={"User-Agent":ua.random,
             "referer":"https://www.jianshu.com/c/a480500350e7",
             "origin":"https://www.jianshu.com",
             "x-csrf-token":"kj3GBF28BYqvYk2554PQE3ghmUbQJGU6WkR9NLon+dlidjzZUArpnKAuyG4Pc0beKOnr9zZkIlEWjh5ESKQkYQ=="
    }
    cookies = "__yadk_uid=jvAQMN7YjInN2SIp6iayfpcX2CT80EoG; UM_distinctid=16b9265ec911a1-0d13cbde3b38e-43450521-15f900-16b9265ec93495; read_mode=day; default_font=font2; locale=zh-CN; _m7e_session_core=5805d7e82cc0a081a5623269ef335326; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1561543937,1561544898,1561601355,1561607378; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216b9265e95b459-00bd3da296b06-43450521-1440000-16b9265e95e597%22%2C%22%24device_id%22%3A%2216b9265e95b459-00bd3da296b06-43450521-1440000-16b9265e95e597%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22index-banner-s%22%7D%7D; CNZZDATA1272960453=1261944565-1561526884-https%253A%252F%252Fwww.baidu.com%252F%7C1561621432; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fp%2F7b91be6fcc45; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1561623720"
    cookie = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
    res = requests.get(url,headers= header)
    print(res.text)
