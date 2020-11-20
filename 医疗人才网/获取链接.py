# coding=utf-8
"""
Author:song
"""
import time
import re

from lxml import etree
import requests
def getlink():
    with open('urllist.txt') as f:
        for url in f:
            print(url)
            while 1:
                headers= {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','referer':'https://www.kq36.com/job_list.asp?Job_ClassI_Id=2'}
                res=requests.get(url,headers=headers)
                if res.status_code == 200:
                    html = etree.HTML(res.text)
                    alist = html.xpath('//td[@class="login"]/a/@href')
                    print(len(alist))
                    with open('detailurl.txt','a') as uu:
                        for i in alist:
                            uu.write("https://www.kq36.com"+i+'\n')

                    time.sleep(2)
                    break
                else:
                    print(res.status_code)
                    time.sleep(60)

def getlistpage():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'referer': 'https://www.kq36.com/job_list.asp?Job_ClassI_Id=2'}
    with open('detailurl.txt') as f:
        zhiwei=[]
        for url in f:
            res = requests.get(url, headers=headers)
            html = etree.HTML(res.text)
            alist = html.xpath('//div[@class="li_title"]/a/@onmouseover')
            # print(alist)
            for i in alist:
                zhiwei.append(re.sub(r'<.*?>','',i[12:-2]).replace(""))
            print(zhiwei)
            exit()

if __name__ == '__main__':
    getlistpage()
