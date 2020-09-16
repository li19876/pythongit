# codeing=utf-8
"""
Author:song
"""
import pymysql
import time
import nb_print
import requests
from lxml import etree

# urllist = ['https://shangbiao.tianyancha.com/l0t'+str(i) for i in range(1,46)]
db = pymysql.connect(host="localhost", port=3306, user="root", password="li123456..", db='lys', charset="utf8")
curosr = db.cursor()


def getres(url):
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
    cookie = 'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; __insp_wid=677961980; __insp_slim=1565856225188; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY2xhaW0vYXBwbHkvMzM2MTM4MTQyMT9wcmljaW5nUGFja2FnZT0wJmVkaXRNb2JpbGU9MQ%3D%3D; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; tyc-user-phone=%255B%252218202610240%2522%255D; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1583198527,1583298144,1583366654,1583922481; bannerFlag=true; _gid=GA1.2.1548451223.1585017829; cloud_token=5fe4ec56c0304f9c9aeac29094456a39; aliyungf_tc=AQAAAEB2BDQKzgUASEwvatSrWxfGHEGP; csrfToken=XtNxROO6rMT3ETZdc7TPz4f_; Hm_lvt_2530ab7750ce2f0d714e3e69613d481b=1585128690; token=6bde4d4261354d479f44a37d00468634; _utm=6e3d249395644c098789108f4ab6e8f2; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A%25223%2522%252C%2522surday%2522%253A%2522125%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522schoolGid%2522%253A%2522%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%252210%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU4NTEzMTkyNiwiZXhwIjoxNjAwNjgzOTI2fQ.Zul7ephCWp4RKZ9Ua1O1CtzGJoFtl302JAp1tmVCC3TkhTnjA0mEdCXWcada_FovYB-F6oi__0lXNWRSiQObIg%2522%252C%2522schoolAuthStatus%2522%253A%25222%2522%252C%2522vipToTime%2522%253A%25221595903278098%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522companyAuthStatus%2522%253A%25222%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E7%25BE%258E%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522isExpired%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522companyGid%2522%253A%2522%2522%252C%2522mobile%2522%253A%252218202610240%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMjYxMDI0MCIsImlhdCI6MTU4NTEzMTkyNiwiZXhwIjoxNjAwNjgzOTI2fQ.Zul7ephCWp4RKZ9Ua1O1CtzGJoFtl302JAp1tmVCC3TkhTnjA0mEdCXWcada_FovYB-F6oi__0lXNWRSiQObIg; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1585131962; _gat_gtag_UA_123487620_1=1; Hm_lpvt_2530ab7750ce2f0d714e3e69613d481b=1585193950'
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
    res = requests.get(url, headers=headers, cookies=cookies)
    return res


def parse(response):
    html = etree.HTML(response.text)
    hreflist = html.xpath('//div[@class="content"]/div[2]/div[2]/a/@href')
    return hreflist


def parse_detail(response):
    html = etree.HTML(response.text)
    item = {}
    item["a"] = html.xpath("string(//td[text()='商标名称']/following-sibling::td[1])")  # 商标名称
    item["b"] = html.xpath("string(//div[@class='logo -w196']/img/@data-src)")  # 商标图片src
    item["c"] = html.xpath("string(//td[text()='申请/注册号']/following-sibling::td[1])")
    item["d"] = html.xpath("string(//td[text()='国际分类']/following-sibling::td[1])")
    item["e"] = html.xpath("string(//td[text()='申请日期']/following-sibling::td[1])")
    item["f"] = html.xpath("string(//td[text()='申请人名称（中文）']/following-sibling::td[1])")
    item["g"] = html.xpath("string(//td[text()='申请人名称（英文）']/following-sibling::td[1])")
    item["h"] = html.xpath("string(//td[text()='申请人地址（中文）']/following-sibling::td[1])")
    item["i"] = html.xpath("string(//td[text()='申请人地址（英文）']/following-sibling::td[1])")
    item["j"] = html.xpath("string(//td[text()='是否共有商标']/following-sibling::td[1])")
    item["k"] = html.xpath("string(//td[text()='商标类型']/following-sibling::td[1])")
    item["l"] = html.xpath("string(//td[text()='专用权期限']/following-sibling::td[1])")
    item["m"] = html.xpath("string(//td[text()='商标形式']/following-sibling::td[1])")
    item["n"] = html.xpath("string(//td[text()='国际注册日期']/following-sibling::td[1])")
    item["o"] = html.xpath("string(//td[text()='后期指定日期']/following-sibling::td[1])")
    item["p"] = html.xpath("string(//td[text()='优先权日期']/following-sibling::td[1])")
    item["q"] = html.xpath("string(//td[text()='代理/办理机构']/following-sibling::td[1])")
    item["r"] = html.xpath("string(//td[text()='初审公告期号']/following-sibling::td[1])")
    item["s"] = html.xpath("string(//td[text()='初审公告日期']/following-sibling::td[1])")
    item["t"] = html.xpath("string(//td[text()='注册公告期号']/following-sibling::td[1])")
    item["u"] = html.xpath("string(//td[text()='注册公告日期']/following-sibling::td[1])")
    item["v"] = html.xpath("string(//td[text()='商标公告']/following-sibling::td[1])")
    item["w"] = html.xpath("string(//td[text()='商品／服务']/following-sibling::td[1])")
    item["x"] = html.xpath("string(//td[text()='商标流程']/following-sibling::td[1])").replace('\xa0',' ')
    return item


def save(item):
    sorted(item)
    values = [v for v in item.values()]
    value = str(values).replace("[", "").replace("]", "")
    sql = "insert into trademark (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x) values ({})".format(value)
    # print(sql)
    try:
        curosr.execute(sql)
        db.commit()
        print('写入了:' + item['a'])
    except Exception as e:
        print(e)
        db.rollback()


def parse_listpage(response):
    html = etree.HTML(response.text)
    url = html.xpath("//div[@class='header']/a/@href")
    return url


def getpage(response):
    html = etree.HTML(response.text)
    resnum = html.xpath('//*[@id="search"]/div[1]/div/div/span/text()')
    if resnum:
        resnum = resnum[0]
        if resnum == "1000+":
            resnum = 1000
        else:
            resnum = int(resnum)
        print("获取页数成功,页数为:{}".format(resnum))
        if resnum == 0:
            return 0
        elif resnum > 999:
            return 50
        else:
            return resnum // 20 + 1
    else:
        return None


"""
:param big 总分类url索引开始位置,从0开始
:param p   从多少页开始,从0开始,传0就是第一页
:param sm  从当前页的多少条开始,值为0-19
"""

def run(big,p,sm):
    urllist = []
    with open("商标url.txt", 'r') as f:
        for i in f:
            urllist.append(i.strip())  # 获取总类别文件url,也就是各分类的url
    for url in urllist[big:]:
        print(url+"索引是:"+str(urllist.index(url)))
        res = getres(url)
        page = getpage(res)
        if page is not None:
            pageurl = [url + "/p" + str(i) for i in range(1, page + 1)]  # 获取分页的url
            for i in pageurl[p:]:
                r = getres(i)
                print('当前分页链接是'+i)
                deteil_urllist = parse_listpage(r)  # 获取详情页url
                for s in deteil_urllist[sm:]:
                    res = getres(s)
                    item = parse_detail(res)
                    save(item)
                    time.sleep(0.5)
        else:
            print("没获取到页数")
            exit()


if __name__ == '__main__':
    # 获取所有分类的url
    # for url in urllist:
    #     res=getres(url)
    #     securl_list=parse(res) # 二级分类的url
    #     for i in securl_list:
    #         res2=getres(i)
    #         finallurl = parse(res2)
    #         with open('商标url.txt','a',encoding='utf-8') as f:
    #             for s in finallurl:
    #                 f.write(s+'\n')
    #                 print('写入了'+s)
    #         time.sleep(2)
    run(0,34,2)
#
