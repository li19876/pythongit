import csv
import nb_print
import requests
import time
import tools
from lxml import etree
url = 'http://jst.sc.gov.cn/xxgx/Enterprise/eLWQYList.aspx'
def getres(VIEWSTATE,EVENTVALIDATION,page):
    session=requests.session()
    header="""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Host: jst.sc.gov.cn
    Pragma: no-cache
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"""
    data="""__VIEWSTATEGENERATOR: 763777C1
__EVENTTARGET: ctl00$MainContent$gvBiddingResultPager
mc: 
xydm: """
    datas=tools.make_header(data)
    datas['__VIEWSTATE'] = VIEWSTATE
    datas['__EVENTVALIDATION'] = EVENTVALIDATION
    datas['__EVENTARGUMENT'] = page
    headers=tools.make_header(header)
    res = session.post(url,headers=headers,data=datas)
    html=etree.HTML(res.text)
    item={}
    item['gsname'] = html.xpath("//table[@class='table  table-striped table-hover table-search-list']/tbody/tr/td[1]/text()")
    item['address'] = html.xpath("//table[@class='table  table-striped table-hover table-search-list']/tbody/tr/td[2]/text()")
    item['name'] = html.xpath("//table[@class='table  table-striped table-hover table-search-list']/tbody/tr/td[3]/text()")
    item['phone'] = html.xpath("//table[@class='table  table-striped table-hover table-search-list']/tbody/tr/td[4]/text()")
    item['VIEWSTATE'] = html.xpath("//input[@name='__VIEWSTATE']/@value")[0]
    item['EVENTVALIDATION'] =html.xpath("//input[@name='__EVENTVALIDATION']/@value")[0]
    item['nowpage']= html.xpath('//td[@class="paginator-custom-data"]/u[1]/text()')[0].split('/')[0]
    item['data'] = list(zip(item['gsname'], item['address'], item['name'], item['phone']))
    return item

def save(item):
    with open('sichuan.csv','a',encoding='gbk',newline='') as f:
        csvwriter=csv.writer(f)
        for i in item['data']:
            csvwriter.writerow(i)
        print('写入完成')

if __name__=='__main__':
    a= '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'
    b='+KQiT6UadREnecRVPJKD4udT2L2rpITB/YV0GOSWU8N1M+IPWe/9IeKqxhjyWuEP8u7EWFZ/4G3yJS9Q5yThGFZy9pQjwHXPACFUG495ZMaja4w63+8QlNhkiHSnDglnUe/c7/2REyA'
    first=getres(a,b,26)
    a = first['VIEWSTATE']
    b = first['EVENTVALIDATION']
    page=first['nowpage']
    save(first)
    # print(first)
    # exit()
    for i in range(1928):
        res = getres(a,b,str(int(page)+1))
        save(res)
        a = res['VIEWSTATE']
        b = res['EVENTVALIDATION']
        page = res['nowpage']
        print('爬取一页，当前页数'+page)
        time.sleep(1)



