import time

import requests
import re
import os
import sys
def get(keyword,page):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'shangbiao.tianyancha.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    url ='https://shangbiao.tianyancha.com/search/{}/p{}'.format(keyword,page)
    cookie='TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; __insp_wid=677961980; __insp_slim=1565856225188; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY2xhaW0vYXBwbHkvMzM2MTM4MTQyMT9wcmljaW5nUGFja2FnZT0wJmVkaXRNb2JpbGU9MQ%3D%3D; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; jsid=SEM-BAIDU-PP-VI-301001; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1574995359,1575967374,1577427146; _gid=GA1.2.272920010.1577427146; RTYCID=bb1b80f2d3fc41a3af52f375f9236a33; CT_TYCID=9b039d9169624b44a8cacf71d5703964; cloud_token=a53846ad75b8432086543b92ec8b9066; bannerFlag=true; aliyungf_tc=AQAAAHyEQVpbBwYArXwvaljnelrHTL9U; csrfToken=s60CO2Rk8zkccTgIKujXaeCE; href=https%3A%2F%2Fip.tianyancha.com%2Ftm%2F35857713t45; Hm_lvt_01daffb1fc8d135428513cb7c4afca15=1577427375; CLOUDID=fea302fe-2ba0-44a4-9897-2c99778df91b; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1577427520; accessId=b3ebcec0-09a9-11ea-b7e1-aff0bff10886; qimo_seosource_b3ebcec0-09a9-11ea-b7e1-aff0bff10886=%E7%AB%99%E5%86%85; qimo_seokeywords_b3ebcec0-09a9-11ea-b7e1-aff0bff10886=; pageViewNum=32; Hm_lpvt_01daffb1fc8d135428513cb7c4afca15=1577433349'
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
    res=requests.get(url,headers=headers,cookies=cookies)
    return res.text


def parse(keyword):

    one=get(keyword,'1')
    with open(os.getcwd()+os.sep+"htmlres/"+keyword+'-1.html','w') as f:
        f.write(one)

    listnum = re.findall(r'找到相关结果<span class="result-num">&nbsp(\d+)</span>&nbsp个',one)
    page = int(listnum[0]) // 30 +1
    if page>1:
        for i in range(2,page+1):
            res = get(keyword,i)
            with open(os.getcwd() + os.sep + "htmlres/" + keyword + '-'+str(i)+'.html', 'w') as f:
                f.write(res)
            print('完成一页,休息1s')
            time.sleep(1)


if __name__=='__main__':
   print(get('技术','3'))

