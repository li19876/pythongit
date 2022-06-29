import requests
import time
import json
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
ua = UserAgent()
""" 参数为浏览器直接复制的header字符串，返回处理好的headers字典 """
def make_header(header_str=''):
    headers = header_str.split('\n')
    # return headers
    headers_dict = {i.split(': ')[0].strip(): i.split(': ')[1].strip() for i in headers}
    return headers_dict

""" 参数为浏览器直接复制的cookie字符串，返回处理好的cookies字典 """
def make_cookie(cookie=''):
    cookies= {i.split("=")[0]:i.split("=")[1] for i in cookie.split(";")}
    return cookies

def getcookie():
    url = 'https://www.ceair.com'
    options = webdriver.ChromeOptions()
 
    # 处理SSL证书错误问题
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--headless")
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
    # 忽略无用的日志
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver.exe')
    with open('./stealth.min.js') as f:
        js = f.read()

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    
    driver.get(url)
    locator = (By.CLASS_NAME, "page-tab-content")
    ele = WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
    c1 = driver.get_cookies()
    cookie = parse_cookie(c1)
    return cookie
def parse_cookie(cookie):
    x={}
    for line in cookie:
        x[line['name']] = line['value']
    return x
def run():
    cookie = """inter=ZWUyMGNjY2QtYjE2Ni00ODA2LTgyODItZTcxMWFmNzc5YWI4; acw_tc=2f6fc11516558752693794068ea295b750b6fefe19c23ce0930d2e5669cf65; C3VK=ff9762; HMF_CI=ce88bff958cec9c3468c092eb5290339ed0c70fdf25f0820e1218109c3b5e260a3; _ga=GA1.2.2122703337.1655875271; _gid=GA1.2.60143000.1655875271; _gat_UA-80008755-11=1; gr_user_id=3e5d51b8-4800-4b6b-828e-92a79eee8980; 84bb15efa4e13721_gr_session_id=e552e43b-9ca7-4d74-adc9-1d1cdf158ee5; 84bb15efa4e13721_gr_session_id_e552e43b-9ca7-4d74-adc9-1d1cdf158ee5=true; HBB_HC=1f7e848209c4a1764b43db6dc746bc9d4916cb32d5570637d83457da7b406acbb361a9c3757977368e2a5f6ff2fe3bc009"""

    cookies = make_cookie(cookie)
    json_data = {
        'flightItems': [
            {
                'depCode': 'EWR,JFK,LGA,SWF',
                'arrCode': 'PVG,SHA',
                'depCityCode': 'NYC',
                'arrCityCode': 'SHA',
                'depDt': '2022-07-04',
                'index': 1,
            },
        ],
        'preference': {
            'cabinRank': 'F,J,Y',
            'currencyCode': 'CNY',
            'lowestControl': '1',
        },
        'routeType': 'OW',
        'deviceId': '',
    }


    for i in range(10000):
        t = time.time()
        r = str(int(round(t * 1000)))[4:-1]+'8'
        # r='287753638'
        header = """authority: www.ceair.com
        method: POST
        path: /portal/v3/shopping/querySummaryPrice
        scheme: https
        accept: application/json, text/plain, */*
        accept-encoding: gzip, deflate, br
        accept-language: zh-CN,zh;q=0.9
        content-length: 245
        content-type: application/json;charset=UTF-8;
        origin: https://www.ceair.com
        referer: https://www.ceair.com/shopping?searchKey=JTdCJTIydHJhdmVsVHlwZSUyMiUzQSUyMm9uZXdheSUyMiUyQyUyMnBhc3Nlbmdlck51bSUyMiUzQSUyMjElMkMwJTJDMCUyMiUyQyUyMmRlcENpdHklMjIlM0ElMjJOWUMlMjIlMkMlMjJhcnJDaXR5JTIyJTNBJTIyU0hBJTIyJTJDJTIyZGVwVmFsdWVzJTIyJTNBJTIyRVdSJTJDSkZLJTJDTEdBJTJDU1dGJTIyJTJDJTIyYXJyVmFsdWVzJTIyJTNBJTIyUFZHJTJDU0hBJTIyJTJDJTIyZGVwQ2l0eU5hbWUlMjIlM0ElMjIlRTUlQjclQjQlRTklQkIlOEUlMjIlMkMlMjJhcnJDaXR5TmFtZSUyMiUzQSUyMiVFNSU4QyU5NyVFNCVCQSVBQyUyMiUyQyUyMmRlcFNlbGVjdFZhbHVlJTIyJTNBJTIyRVdSJTJDSkZLJTJDTEdBJTJDU1dGJTIyJTJDJTIyYXJyU2VsZWN0VmFsdWUlMjIlM0ElMjJQVkclMkNTSEElMjIlMkMlMjJkZXBMYWJlbCUyMiUzQSUyMiUyMiUyQyUyMmFyckxhYmVsJTIyJTNBJTIyJTIyJTJDJTIyaXNBcnJDaXR5JTIyJTNBdHJ1ZSUyQyUyMmlzRGVwQ2l0eSUyMiUzQXRydWUlMkMlMjJkYXRlJTIyJTNBJTIyMjAyMi0wNy0wNCUyMiUyQyUyMmNhYmluQ2xhc3MlMjIlM0ElMjJBTEwlMjIlMkMlMjJwYXlXYXklMjIlM0ElMjJtb25leSUyMiUyQyUyMnQlMjIlM0ExNjU1ODcwOTExNzQ0JTdEENCODEKEY
        sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"
        sec-ch-ua-mobile: ?0
        sec-ch-ua-platform: "Windows"
        sec-fetch-dest: empty
        sec-fetch-mode: cors
        sec-fetch-site: same-origin
        shakehand: 5422a8dc0f588a184f238940de1feb07
        site: zh_CN
        user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36
        x-tingyun-id: DuR5xFLm8eI;r={}""".format(r)
        headers = make_header(header)
        # headers['user-agent'] = ua.random
        
        response = requests.post('https://www.ceair.com/portal/v3/shopping/querySummaryPrice', cookies=cookies, headers=headers, json=json_data)
        text = response.text
        try:
            print(text)
            print(json.loads(text))
            print('运行次数：', i)
            time.sleep(30)
        except Exception as e:
            print('出错了，去获取cookie')
            try:
                cookies = getcookie()
                print('获取cookie成功:', cookies)
                time.sleep(5)
            except:
                print('获取cookie失败,休息5分钟')
                time.sleep(60*5)
        # print(response.headers)
        # print(dir(response))

if __name__ == '__main__':
    run()
    # print(os.getcwd())