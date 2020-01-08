import requests


def get(keyword):
    url = 'https://api.duyandb.com/search/search/queryByExp'
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization':"",
        'Content-Length':"120",
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type':'application/json',
        'Origin':'https://www.uyanip.com',
        'Pragma':'no-cache',
        'Host': 'api.duyandb.com',
        'Referer': 'https://www.uyanip.com/result?exp=KEYWORD:(%E6%B7%B1%E5%9C%B3%E5%B7%B4%E6%96%AF%E5%B7%B4%E7%A7%91%E6%8A%80%E5%8F%91%E5%B1%95%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8)',
        'secret':"f2b68f0113577353dfaf0b5a2eba3071",
        'uuid': '01b47b5e-abc0-41b8-8791-e540407829d7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    data = {
        'exp':'KEYWORD:(深圳巴斯巴科技发展有限公司)'.encode("utf-8"),
        'highlight':'True',
        'page':'1',
        'pageSize':'20',
        'sort':'0',
        'un_exp':''
    }
    res = requests.post(url,headers=headers,data=data)
    print(res.text)

if __name__=='__main__':
    get('12')