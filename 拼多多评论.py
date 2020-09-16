# coding=utf-8
"""
Author:song
"""
import requests

from tools import *
url = 'https://mobile.yangkeduo.com/proxy/api/reviews/7103840488/list?pdduid=0&page={}&size=10&enable_video=1&enable_group_review=1&label_id=0'
header=""":authority: mobile.yangkeduo.com
:method: GET
:path: /proxy/api/reviews/7103840488/list?pdduid=0&page=5&size=10&enable_video=1&enable_group_review=1&label_id=0
:scheme: https
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
pragma: no-cache
user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"""
headers=make_header(header)
cookies=make_cookie("api_uid=CiSqEF6G905E2QBPSHQ7Ag==; ua=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F69.0.3497.100%20Safari%2F537.36; _nano_fp=XpdJnpUoXqTYn5dJX9_twGje9GGMylfYQXYSaslZ; webp=1")
res= requests.get(url,headers=headers,cookies=cookies)
print(res.text)





