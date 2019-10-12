from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import re
import json
from lxml import etree
from getip import getip
import randphoneua
ci='10'
# 返回一个ip和对应的cookie，cookie以字符串形式返回。ip需要经过测试
def get_cookie(refalsh=0):
    mark = 0
    while mark == 0:
        # 购买的ip获取地址
        ip = getip(refalsh)
        uas = randphoneua.randua()
        try:
            val = '--proxy-server=http://' + ip
        except TypeError:
            time.sleep(1)
            ip = getip()
            val = '--proxy-server=http://' + ip
        ua = 'user-agent=' + uas
        val2 = 'http://' + ip
        p = {'http': val2}
        print('获取IP：', p)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(val)
        chrome_options.add_argument(ua)
        driver = webdriver.Chrome(options=chrome_options)
        # driver.set_page_load_timeout(8)  # 设置超时
        # driver.set_script_timeout(8)
        url = 'https://i.meituan.com/shanghai/'  # 美团深圳首页
        url2 = 'https://meishi.meituan.com/i/?ci='+ci+'&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1'  # 美食页面
        try:
            driver.get(url)
            driver.get(url)
            locator = (By.CLASS_NAME, "msg-bd")
            ele = WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
            time.sleep(1)
            quxiao = driver.find_element_by_xpath("//div[@id='msg']/div[2]/span[2]")
            actions = ActionChains(driver)
            actions.move_to_element_with_offset(quxiao, 10, 10).click().perform()
            time.sleep(5)
            c1 = driver.get_cookies()
            time.sleep(1)
            driver.get(url2)
            time.sleep(3)
            js = 'var q=document.documentElement.scrollTop=100'
            driver.execute_script(js)
            time.sleep(1)
            url3 = driver.find_element_by_xpath("//div[@class='list']/a[1]").get_attribute("href")
            driver.get(url3)
            # actions.click(dta).perform()

            time.sleep(3)
            c = driver.get_cookies()
            driver.quit()
            print('*******************')
            print(len(c1), len(c))
            # 判断cookie是否完整，正常的长度应该是18
            if len(c) > 20:
                mark = 1
                # print(c)
                x = {}
                for line in c:
                    x[line['name']] = line['value']
                # 将cookie合成字符串，以便添加到header中，字符串较长就分了两段处理
                # co1 = '__mta=' + x['__mta'] + '; client-id=' + x['client-id'] + '; IJSESSIONID=' + x[
                #     'IJSESSIONID'] + '; iuuid=' + x[
                #           'iuuid'] + '; meishi_ci=30; ci=30; ci3=1; cityname=%E6%B7%B1%E5%9C%B3; logan_custom_report=; latlng=; webp=1; _lxsdk_cuid=' + x[
                #           '_lxsdk_cuid'] + '; _lxsdk=' + x['_lxsdk'] + '; logan_session_token=' + x['logan_session_token']
                # co2 = '; __utma=' + x['__utma'] + '; __utmc=' + x['__utmc'] + '; __utmz=' + x[
                #     '__utmz'] + '; __utmb=' + x['__utmb'] + '; i_extend=' + x['i_extend'] + '; uuid=' + x[
                #           'uuid'] + '; _hc.v=' + x['_hc.v'] + '; _lxsdk_s=' + x['_lxsdk_s']
                # co = co1 + co2
                co = '; '.join(item for item in [item["name"] + "=" + item["value"] for item in c])

                print(co)
                return (p,co,ua)
            else:
                print('缺少Cookie,长度：', len(c))

        except Exception as e:
            print("发生了异常"+str(e))
            driver.quit()


    # 解析店铺详情页面，返回店铺信息info和一个标志位mark
    # 传入参数u包含url和店铺分类，pc包含cookie和ip，m代表抓取的数量，n表示线程号，ll表示剩余店铺数量，ttt该线程抓取的总时长


def parse(u, pc, m, n, ll, ttt):
    mesg = 'Thread:' + str(n) + ' No:' + str(m) + ' Time:' + str(ttt) + ' left:' + str(ll)  # 记录当前线程爬取的信息
    url = u[0]
    cate = u[1]
    id  = u[2]
    p = pc[0]
    ua = pc[2]
    cookie = pc[1]
    mark = 0  # 标志位，0表示抓取正常，1,2表示两种异常
    head = {'Host': 'meishi.meituan.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma':'no-cache',
            'Referer': 'https://meishi.meituan.com/i/?ci='+ci+'&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
            'User-Agent': ua,
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'same-site',
            'Sec-Fetch-User':'?1'

            }
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie.split("; ")}
    info = []  # 店铺信息存储
    try:
        r = requests.get(url, headers=head, timeout=3, proxies=p,cookies=cookies)
        print(url)
        # print(r.text)
        r.encoding = 'utf-8'
        html = etree.HTML(r.text)
        datas = html.xpath('//script[@crossorigin="anonymous"]')
        if datas ==[]:
            print(r.text)
            mark = 1
            info= ""
            return (mark,info)
        for data in datas:
            try:
                if re.match("window\._appState",data.text):
                    print("解析成功")
                    result = data.text[19:-1]
                    result = json.loads(result)
                    name = result['poiInfo']['name']
                    addr = result['poiInfo']['addr']
                    phone = result['poiInfo']['phone']
                    aveprice = result['poiInfo']['avgPrice']
                    opentime = result['poiInfo']['openInfo']
                    opentime = opentime.replace('\n', ' ')
                    avescore = result['poiInfo']['avgScore']
                    marknum = result['poiInfo']['MarkNumbers']
                    lng = result['poiInfo']['lng']
                    lat = result['poiInfo']['lat']
                    info = [id,name, cate, addr, phone, aveprice, opentime, avescore, marknum, lng, lat]
                    print(id,mesg, name, cate, addr, phone, aveprice, opentime, avescore, marknum, lng, lat)

            except:
                pass
    except Exception  as e:
        print('Error  Thread:', n)  # 打印出异常的线程号
        print(e)
        s = str(e)[-22:-6]
        if s == '由于目标计算机积极拒绝，无法连接':
            print('由于目标计算机积极拒绝，无法连接', n)
            mark = 1  # 1类错误，需要更换ip
        else:
            mark = 2  # 2类错误，再抓取一次
    return (mark, info)  # 返回标志位和店铺信息
