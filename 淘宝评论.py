import requests
import random
import time
import json
import re
def getres(page,sellerid,supid,itemid):
    headers= {
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'referer':'https://detail.tmall.com/item.htm?spm=a230r.1.14.43.5f8c442bUhESAt&id=597087667969&ns=1&abbucket=1',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    cookie = 'hng=CN%7Czh-CN%7CCNY%7C156; lid=tb76332162; enc=88PIjMqzNcPv6Df0dyro90GV8HPXtb44bz%2FyEQ4hOPhK%2FVwnaNBQfcjZuO%2FjyLF2rrlpskr3oSn23ITi1Z8pzw%3D%3D; cna=0/WZFcFaezkCAWovfr4ENWUt; uc1=cookie14=UoTaG7bU%2Fz8oaw%3D%3D; t=f01a5b4cad227455f715279316ec3df4; uc3=vt3=F8dBy34Q7WQd3CEjitA%3D&id2=UonZBGYblmDoGg%3D%3D&nk2=F5RCY8KJ0HvtyQ%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; tracknick=tb76332162; lgc=tb76332162; _tb_token_=538660ee3e83b; cookie2=5f2b68406c45aaef77702dd82ad38860; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; l=cBT3xzVrqrwuRl-vBOfNNuI8av_t5QAbCsPzw4_gQIB19l14sdQPeHwQbWv2U3QQE95jweKroqC0SRUeSuU_Wx_ceTwhKXIpB; isg=BF1deVoM3MvJdbj95KN8uDk1bDmX0pFV1a2F-B8g6LZt1noI5smgnikAAIr1FqmE'
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
    aa = random.randint(1000,9999)
    url = "https://rate.tmall.com/list_detail_rate.htm?itemId={}&spuId={}&sellerId={}&order=3" \
          "&currentPage={}&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098" \
          "%23E1hvlvvWvRyvUvCkvvvvvjiPRFMysjtWRFFZgjYHPmPOAjiPP2qWAjYWR2qU0j1HRphvCvvvvvmrvpvEvvFzh9hCv8vz3QhvCvvhvvmtvpvIvvvvvhCvvvvvvUjQphvUDQvvvACvpvQovvv2UhCv2jhvvvW9phvWwOyCvvOUvvVvay%2FivpvUvvmvneVSPoZEvpCWmmIWvvwAgb2XSfpAOH2%2BFOcn%2B3C1pKFEDaVTRogRD7z9aXTAVAnldUFB83H%2BCNLwlWAwHFXXiXVvQE01Ux8x9WLpjLyDZacEKOmAdphCvvOvCvvvphvPvpvhvv2MMsyCvvpvvvvviQhvCvvv9U8CvpvZz21fNdMNznswUBrfq0NG%2Fr197Ih%3D&needFold=0&_ksTS={}_{}&callback=jsonp{}".format(itemid,supid,sellerid,page,int(time.time()),aa,aa+1)
    res = requests.get(url,headers=headers,cookies=cookies)
    js = re.sub(r"jsonp\d\d\d\d\(","",res.text)[0:-1]
    bb=json.loads(js)
    return bb

# print(bb)
def getid(url):
    itemid = re.findall(r"id=\d+&",url)[0][3:-1]
    print(itemid)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control':'max-age=0',
        'upgrade-insecure-requests':'1',
        'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.43.5f8c442bUhESAt&id=597087667969&ns=1&abbucket=1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    cookie = 'hng=CN%7Czh-CN%7CCNY%7C156; lid=tb76332162; enc=88PIjMqzNcPv6Df0dyro90GV8HPXtb44bz%2FyEQ4hOPhK%2FVwnaNBQfcjZuO%2FjyLF2rrlpskr3oSn23ITi1Z8pzw%3D%3D; cna=0/WZFcFaezkCAWovfr4ENWUt; uc1=cookie14=UoTaG7bU%2Fz8oaw%3D%3D; t=f01a5b4cad227455f715279316ec3df4; uc3=vt3=F8dBy34Q7WQd3CEjitA%3D&id2=UonZBGYblmDoGg%3D%3D&nk2=F5RCY8KJ0HvtyQ%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; tracknick=tb76332162; lgc=tb76332162; _tb_token_=538660ee3e83b; cookie2=5f2b68406c45aaef77702dd82ad38860; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; l=cBT3xzVrqrwuRl-vBOfNNuI8av_t5QAbCsPzw4_gQIB19l14sdQPeHwQbWv2U3QQE95jweKroqC0SRUeSuU_Wx_ceTwhKXIpB; isg=BF1deVoM3MvJdbj95KN8uDk1bDmX0pFV1a2F-B8g6LZt1noI5smgnikAAIr1FqmE'
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
    res = requests.get(url, headers=headers, cookies=cookies)
    sellerid = re.findall(r'"sellerId":\d+,',res.text)[0][11:-1]
    supid = re.findall(r'"spuId":"\d+"',res.text)[0][9:-1]
    return {"sellerid":sellerid,"supid":supid,"itemid":itemid}
    # print(sellerid)
    # print(supid)
    # print(itemid)

def run():
    url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.97.5f8c442bUhESAt&id=591297366951&ns=1&abbucket=1"
    id = getid(url)
    for page in range(10):
        bb = getres(page,id["sellerid"],id["supid"],id["itemid"])
        pllist = bb["rateDetail"]["rateList"]
        for i in pllist:
            print("评论:"+i["rateContent"])
            if i["appendComment"] != None:
                print("追评是:"+i["appendComment"]["content"])
        time.sleep(1)
if __name__ =="__main__":
    run()
