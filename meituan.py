# -*- coding:utf-8 -*-
import json
import os
import random
import requests
# import get_cookies
import time

# 全局时间量
date = time.strftime('%Y-%m-%d', time.localtime())

def is_file():
    try:
        os.mkdir('./' + date + '/')
    except:
        pass

def crow_id(cookie,offset):
    url='https://meishi.meituan.com/i/api/channel/deal/list'
    head={'Host': 'meishi.meituan.com',
          'Accept': 'application/json',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
          'Referer': 'http://meishi.meituan.com/i/?ci=325&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
          'User-Agent': '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
          'Cookie':cookie
                    }
    # p = {'https': 'https://27.157.76.75:4275'}
    data={"uuid":"6cc394bd-6f09-4ba0-92c7-2d8c1cfe178f",
          "version":"8.3.3",
          "platform":3,
          "app":"",
          "partner":126,
          "riskLevel":1,
          "optimusCode":10,
          "originUrl":"http://meishi.meituan.com/i/?ci=30&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1",
          "offset":offset,
          "limit":15,
          "cateId":1,
          "lineId":0,
          "stationId":0,
          "areaId":0,
          "sort":"default",
          "deal_attr_23":"",
          "deal_attr_24":"",
          "deal_attr_25":"",
          "poi_attr_20043":"",
          "poi_attr_20033":""}
    r=requests.post(url,headers=head,data=data)#,proxies=p)
    result=json.loads(r.text)
    return result

def run():
    is_file()  # 判断并创建文件夹
    x = 0
    y = 15 # 目标区域门店目录页数，获取方式为当前栏目下totalCount/当前页面显示条数
    while x < y:
        x+=1
        print('当前进度第 : %s 页'%(x), end='\n')
        time.sleep(random.randint(2, 5))
        cookie = open('./cookies.txt', "r", encoding='utf-8').read()
        info=crow_id(cookie,x*30)
        if info['data']['poiList']['totalCount']==0:
            pass
            '''
            功能：更新cookies
            '''
            # print("获取cookie！！！")
            # get_cookies.run('beijing') # cookie错误时调取get_cookies函数，获取最新cookie
            # cookie = open('./cookies.txt', "r", encoding='utf-8').read()
            # info = crow_id(cookie, x * 30)
        elif info['data']['poiList']['totalCount']!=0 and x==0:
            y=info['data']['poiList']['totalCount']/10
        else:
            pass
        dic = {
            'info': info
        }
        with open('./'+date +'/'+str(x) + '.txt', 'w', encoding='utf8') as f:
            json.dump(dic, f)
    print("完成")

if __name__ == '__main__':
    run()