# coding=utf-8
"""
Author:song
"""
import json
import time
import uuid
import requests
import urllib.parse
mac = hex(uuid.getnode())[2:]

url='http://www.hzsrwx.com/ys/license.html'

while 1:
    res=requests.post(url,data={'mac':mac})
    returns=json.loads(res.text.encode('utf8').decode('unicode_escape'))
    if returns["code"] == 1:
        pass
    else:
        print(returns['msg'])
        exit()
    time.sleep(300)


