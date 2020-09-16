# coding=utf-8
"""
Author:song
"""
import os
import time

import requests
import tools
urlfile = './img.txt' #链接存储文件，txt格式
urllist=[]
with open(urlfile) as f:
    for i in f:
        urllist.append(i.strip())
resdir = '小程序图片'
isExists = os.path.exists(resdir)
if not isExists:
    os.mkdir(resdir)
    os.chdir(resdir)
else:
    os.chdir(resdir)
for url in urllist:
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    res=requests.get(url,headers=headers)
    filename=url.split('/')[-1]
    with open(filename,'wb') as img:
        img.write(res.content)
    time.sleep(1)
    print(str(urllist.index(url))+'已完成')

