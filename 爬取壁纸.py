import time
import now
import requests
from lxml import etree

def get_res(url):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'referer':'http://bizhi.bcoderss.com/tag/4k/',
        'host':'bizhi.bcoderss.com',
        'X-Requested-With':'XMLHttpRequest'
    }
    res = requests.get(url,headers=headers)
    return res
if __name__=='__main__':
    with open("urllist.txt",'r') as f:
        urllist = [i for i in f]
    while urllist:
        try:
            url = urllist.pop(0)
            res = get_res(url)
            html = etree.HTML(res.text)
            # 获取下页链接
            imgurl = html.xpath("//div[@class='single-wallpaper']/img/@src")
            if imgurl:
                tmp_img=get_res(imgurl[0])
                with open('4k/'+imgurl[0].split('/')[-1],'wb') as im:
                    im.write(tmp_img.content)
            print(now.now(),"写入了:",imgurl[0].split('/')[-1])
            with open('urllist.txt','w') as p:
                for i in urllist:
                    p.write(i+'\n')
            time.sleep(1)
        except Exception as e:
            with open('urllist.txt','w') as p:
                for i in urllist:
                    p.write(i+'\n')
            print('出错了,休息3s继续')
            time.sleep(3)