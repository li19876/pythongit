import pymysql
import requests
from fake_useragent import UserAgent
from lxml import etree
import time


ua=UserAgent()
db = pymysql.connect(host="127.0.0.1",port = 3306,user="root",password="li123456..",db="lys",charset="utf8")
cursor=db.cursor()


def getres(keyword):
    url = "https://www.qichacha.com/search?key=" + keyword
    headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'www.qichacha.com',
            'Referer':'https://www.qichacha.com/',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    cookie = 'acw_tc=2a51048615615228072143630e576e6af9a9327055e91154b058167ad9; QCCSESSID=3rrstgv419v5p8os2l7k8negi4; UM_distinctid=16bc0cc2237269-0db8398c21bdc-43450521-15f900-16bc0cc223823; zg_did=%7B%22did%22%3A%20%2216bc0cc22a47db-0e94e8fb424428-43450521-15f900-16bc0cc22a5bf0%22%7D; _uab_collina=156230773240331892629544; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1562643505,1562645633,1562645765,1562727763; hasShow=1; CNZZDATA1254842228=723263571-1562306536-https%253A%252F%252Fwww.baidu.com%252F%7C1562738690; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201562740528506%2C%22updated%22%3A%201562741657289%2C%22info%22%3A%201562307732138%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22815c37b1963e2b7252cc310087050e85%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1562741657'
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code == 200:
        print("访问成功")
        return response
    else:
        print(response)
        print(response.text)
        return response.status_code
def parse(keyword):
    print("开始解析")
    result = getres(keyword)
    if not isinstance(result,int):
        html = etree.HTML(result.text)
        resnum = html.xpath("//span[@id='countOld']/span/text()")[0].strip()
        if int(resnum) > 0 :
            gsname = html.xpath("string(//tbody[@id='search-result']/tr[1]/td[3]/a)")
            frname = html.xpath("string(//tbody[@id='search-result']/tr[1]/td[3]/p/a)")
            phone = html.xpath("string(//tbody[@id='search-result']/tr[1]/td[3]/p[2]/span)")
            return {"gsname":gsname,"frname":frname,"phone":phone}
        else:
            return None
    return result
def run():
    sql = """
        select gsname,lxdh from jzw where (lxdh = "联系电话：")
    """
    cursor.execute(sql)
    bb = cursor.fetchall()
    for i in bb:
        res=parse(i[0])
        if isinstance(res,int):
            print(res)
            break
        if res != None:
            update = """
                update jzw set lxr = '{}',lxdh = '{}',gsname = '{}' where gsname = '{}'
            """.format("联系人："+res["frname"],res["phone"],res["gsname"],i[0])
            try:
                cursor.execute(update)
                db.commit()
                print("写入了:{},{},{}".format(res["gsname"],"联系人："+res["frname"],res["phone"]))
            except:
                db.rollback()
        else:

            del1 = """
                delete from jzw where gsname = '{}' 
            """.format(i[0])
            cursor.execute(del1)
            db.commit()
            print("{}没找到,干掉了~".format(i[0]))

        time.sleep(1)

if __name__ =="__main__":
    run()