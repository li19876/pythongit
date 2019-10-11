import requests
url = 'https://xueqiu.com/service/v5/stock/screener/screen?category=CN&size=400&order=desc&order_by=follow7d&only_count=0&page=1&_=1565505200000s'
headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'xueqiu.com',
        'Referer':'https://xueqiu.com/hq',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
cookie="aliyungf_tc=AQAAAAEvmXTu7gsAKn0vahT9hX96luYr; acw_tc=2760820815681827327953312e9fb974fd735918f5de9c2517e44fa469c4d9; xq_a_token=75661393f1556aa7f900df4dc91059df49b83145; xq_r_token=29fe5e93ec0b24974bdd382ffb61d026d8350d7d; u=241568182733553; device_id=24700f9f1986800ab4fcc880530dd0ed; s=bw16nemgl8; __utma=1.1516805567.1568182774.1568182774.1568182774.1; __utmc=1; __utmz=1.1568182774.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1568182776; __utmb=1.4.10.1568182774; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1568183104"
cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
res= requests.get(url,headers=headers,cookies=cookies)
print(res.text)