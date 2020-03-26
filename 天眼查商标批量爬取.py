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
    cookie = 'TYCID=f2564d2097f311e9b4169345e5b2d504; undefined=f2564d2097f311e9b4169345e5b2d504; ssuid=4261586970; _ga=GA1.2.238743067.1561540964; __insp_wid=677961980; __insp_slim=1565856225188; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY2xhaW0vYXBwbHkvMzM2MTM4MTQyMT9wcmljaW5nUGFja2FnZT0wJmVkaXRNb2JpbGU9MQ%3D%3D; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; jsid=SEM-BAIDU-PP-VI-301001; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1574995359,1575967374,1577427146; _gid=GA1.2.272920010.1577427146; RTYCID=bb1b80f2d3fc41a3af52f375f9236a33; CT_TYCID=9b039d9169624b44a8cacf71d5703964; cloud_token=a53846ad75b8432086543b92ec8b9066; bannerFlag=true; aliyungf_tc=AQAAAHyEQVpbBwYArXwvaljnelrHTL9U; csrfToken=s60CO2Rk8zkccTgIKujXaeCE; href=https%3A%2F%2Fip.tianyancha.com%2Ftm%2F35857713t45; Hm_lvt_01daffb1fc8d135428513cb7c4afca15=1577427375; CLOUDID=fea302fe-2ba0-44a4-9897-2c99778df91b; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1577427520; accessId=b3ebcec0-09a9-11ea-b7e1-aff0bff10886; qimo_seosource_b3ebcec0-09a9-11ea-b7e1-aff0bff10886=%E7%AB%99%E5%86%85; qimo_seokeywords_b3ebcec0-09a9-11ea-b7e1-aff0bff10886=; pageViewNum=32; Hm_lpvt_01daffb1fc8d135428513cb7c4afca15=1577433349'
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
    item["x"] = html.xpath("string(//td[text()='商标流程']/following-sibling::td[1])")
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
        print('写入了:' + value)
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


def run():
    urllist = []
    with open("商标url.txt", 'r') as f:
        for i in f:
            urllist.append(i.strip())  # 获取总类别文件url,也就是各分类的url
    for url in urllist:
        print(url)
        res = getres(url)
        page = getpage(res)
        if page is not None:
            pageurl = [url + "/p" + str(i) for i in range(1, page + 1)]  # 获取分页的url
            for i in pageurl:
                r = getres(i)
                deteil_urllist = parse_listpage(r)  # 获取详情页url
                for s in deteil_urllist:
                    res = getres(s)
                    item = parse_detail(res)
                    save(item)
                    time.sleep(1)
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
    run()
#
