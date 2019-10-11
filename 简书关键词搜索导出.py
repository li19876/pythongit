import requests
import json
import time
import re
import csv
from fake_useragent import UserAgent
ua= UserAgent()
with open("文章.csv","a",encoding="utf-8",newline="") as fp:
    csv_write = csv.writer(fp,dialect='excel')
    csv_write.writerow(["标题","链接","简介"])
    for i in range(2,101):
        url = "https://www.jianshu.com/search/do?q=python&type=note&page="+str(i)+"&order_by=default"
        header ={"User-Agent":ua.random,
                 "referer":"https://www.jianshu.com/search?q=python&page=3&type=note",
                 "origin":"https://www.jianshu.com",
                 "x-csrf-token":"dUSJutkDr+3k1dSAIYjbj8mRWa/exFMXkEzJh+4cjAGFD3Nn1LVD++uZUVfJeE1CmVkrHjiEFHzchqr3HJ9RuQ=="
        }
        cookies = "__yadk_uid=jvAQMN7YjInN2SIp6iayfpcX2CT80EoG; UM_distinctid=16b9265ec911a1-0d13cbde3b38e-43450521-15f900-16b9265ec93495; read_mode=day; default_font=font2; locale=zh-CN; _m7e_session_core=5805d7e82cc0a081a5623269ef335326; CNZZDATA1272960453=1261944565-1561526884-https%253A%252F%252Fwww.baidu.com%252F%7C1561605217; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1561543937,1561544898,1561601355,1561607378; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216b9265e95b459-00bd3da296b06-43450521-1440000-16b9265e95e597%22%2C%22%24device_id%22%3A%2216b9265e95b459-00bd3da296b06-43450521-1440000-16b9265e95e597%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22index-banner-s%22%7D%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3Dpython%26page%3D3%26type%3Dnote; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1561608318"
        cookie = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        data = {
            "q":"python",
            "type":"note",
            "page":str(i),
            "order_by":"default"
        }
        res = requests.post(url,headers= header,data=data,cookies=cookie)
        res = json.loads(res.text)
        wzurl = "https://www.jianshu.com/p/"
        data=[]

        for i in res["entries"]:
            print("标题是：",re.sub(r'<.*?>','',i["title"]))
            print("链接是：","https://www.jianshu.com/p/"+i["slug"])
            data.append(re.sub(r'<.*?>','',i["title"]))
            data.append(wzurl+re.sub(r'<.*?>','',i["slug"]))
            data.append(re.sub(r'<.*?>','',i["content"]))
            csv_write.writerow(data)
            data=[]
        print("写入完成")
        time.sleep(1)
