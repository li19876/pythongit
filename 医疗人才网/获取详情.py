# coding=utf-8
"""
Author:song
"""
import time
from fake_useragent import UserAgent
import pymysql
import requests
import urllib3
import nb_print
import proxies
import re
import tools
from lxml import etree
db = pymysql.connect(host="localhost", port=3306, user="root", password="li123456..", db='lys', charset="utf8")
curosr = db.cursor()
ua =UserAgent()
urllib3.disable_warnings()
def getlink():
    sql = "select url from kq36 where email is null"
    curosr.execute(sql)
    res= curosr.fetchall()
    res = [['https://www.kq36.com'+i[0]] for i in res]
    return res

def getlxfs(res):
    html = etree.HTML(res)
    contact = html.xpath('string(//div[@class="left"]/div/table[2])')
    contact = re.sub('[\t\n\r\f\v]', '', contact)
    contact = re.sub('function.+hidden;}', '', contact)
    contact = re.sub('function.+地图/导航', '', contact)
    contact = re.sub('分享招聘海报.+click\(', '', contact)
    contact = re.sub(' ', '', contact)
    contact = re.sub('\xa0', '', contact)
    contact = contact.replace('QQ：', '^QQ：').replace('电话号码：', '^电话号码：').replace('举报单位', '').replace('邮箱：', '^邮箱：').replace(
        '微信号：', '^微信号：').replace('招聘网址', '^招聘网址：').replace('地　　址：', '^地址：').replace('公交/地铁：', '^公交/地铁：').replace(
        '提示：收取费用或押金都可能有欺诈嫌疑，请举报，有效举报奖励200元', '')
    try:
        contact = {i.split("：")[0]: i.split("：")[1] for i in contact.split('^')}
        return contact
    except IndexError:

        print('联系方式解析错误：'+contact)



def delete(url):
    sql = """delete from kq36 where url ='{}'""".format(url.replace('https://www.kq36.com',''))
    try:
        curosr.execute(sql)
        db.commit()
        print(url+'没有了，已删除')
    except Exception as e:
        print(str(e))
def save(item):
    sql = "update kq36 set posttime = '{}',email ='{}',phone='{}',wechat='{}',detail_address='{}' where url = '{}'".format(item['posttime'],item['email'],item['phone'],item['wechat'],item['detail_address'],item['url'])
    try:
        curosr.execute(sql)
        db.commit()
        print(item['url'])
    except Exception as e:
        print('存储错误'+str(e))
def getinfo():
    linklist=getlink()
    header = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Host: www.kq36.com
Pragma: no-cache
Referer: https://www.kq36.com/job_list.asp?Job_ClassI_Id=2&provinceid=12%0A&cityid=421&page=5
Upgrade-Insecure-Requests: 1"""
    cookie = """showjobpop=1; Hm_lvt_c58e42b54acb40ab70d48af7b1ce0d6a=1605492059; ASPSESSIONIDSSRRRCRA=KDEIHLMACPJEKAJGENGBHJJP; ASPSESSIONIDCCQRQBTD=HKCMMFMCJOFALEOKJFOGILNL; ASPSESSIONIDSSATQCTC=LDCJHOGDKAHEONOEDLODFAFJ; ASPSESSIONIDCADRSCRA=OIJLEKLCKDFNHHKJJOMALJOC; ASPSESSIONIDSSSARDSA=IILGPCGDMABLGBNCCDFFFDMF; fikker-DCla-DcOG=MJO9HqOLVO47bJbLO98wRSNNhujMK5FW; fikker-DCla-DcOG=MJO9HqOLVO47bJbLO98wRSNNhujMK5FW; Hm_lpvt_c58e42b54acb40ab70d48af7b1ce0d6a=1606360955"""
    cookies = tools.make_cookie(cookie)
    headers = tools.make_header(header)
    headers['User-Agent'] = ua.random
    headers['Proxy-Authorization'] = proxies.getauth()
    for url in linklist:
        print('开始爬取：'+url[0])
        item={}
        res = requests.get(url[0],headers=headers,cookies=cookies,proxies={'https':'https://dynamic.xiongmaodaili.com:8088'},verify=False,allow_redirects=False,timeout=10)
        if res.status_code == 302:
            delete(url[0])
            continue
        if res.status_code !=503:

            posttime = re.findall(r'发布时间：</span><span class="font_color font14">(.+)</span>',res.text)
            posttime =posttime[0] if posttime else ''
            # print(res.text)
            print('当前状态码',res.status_code)

            lxfs = getlxfs(res.text)

            print(lxfs,posttime)
            item['wechat'] =lxfs['微信号']
            item['email'] = lxfs['邮箱']
            item['phone'] = lxfs['电话号码']
            item['detail_address'] = lxfs['地址']
            item['posttime'] = posttime
            item['url'] = url[0].replace('https://www.kq36.com','')
            save(item)
            time.sleep(1)
        else:
            print('被封了，休息10s')
            time.sleep(10)

if __name__ == '__main__':
    while 1:
        try:
            getinfo()
            break
        except Exception as f:
            print(str(f))
            continue