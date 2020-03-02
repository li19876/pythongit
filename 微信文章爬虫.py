from selenium import webdriver
import time , requests
from lxml import etree
from pyquery import PyQuery as pq
import re



url = 'https://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MzA5MjMwNzc4MQ==&uin=NzgyNjg2NjQy&key=ff1b1d089c15295c9e9abba5ef2a80c18e239346467ae3ac08da1becccd32c52a6e2f956b87aa5f197240bc7c2766b1d0c860a2afb50c3a464fce941a0923942863d4eb86ef06fc798bea22f4139d4f2&devicetype=Windows+7&version=6208006f&lang=zh_CN&ascene=7&pass_ticket=mmk9aZiuxirN0X0YkveOPGzmOXzIlAWrhRteHGslT05KkYD8nyaEYjBUS1BVCIex'
# Chromedriver
opt = webdriver.ChromeOptions()
# prefs = {'profile.default_content_setting_values': {'images': 2}}
# opt.add_experimental_option('prefs', prefs)#这两行是关闭图片加载
opt.add_argument('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.884.400 QQBrowser/9.0.2524.400')#设置headers
# # opt.add_argument('--headless')#此行打开无界面
driver = webdriver.Chrome(options=opt)

driver.get(url)

top = 1
while 1:
    html = etree.HTML(driver.page_source)
    downss = html.xpath('//*[@id="js_nomore"]/div/span[1]/@style')
    if downss[0] == "display: none;":
        time.sleep(0.5)
        js = "var q=document.documentElement.scrollTop="+str(top*20000)
        driver.execute_script(js)#模拟下滑操作
        top += 1
        time.sleep(1)
    else:
        break
html = etree.HTML(driver.page_source)
bodyContent = html.xpath('//*[@id="js_history_list"]/div/div/div/div/h4/@hrefs')#获取文章的所有链接
title = html.xpath('string(//*[@id="js_history_list"]/div/div/div/div/h4)').strip()
#保存本地
fp = open("./aother.txt", "w+")
for i in bodyContent:
    fp.write(str(i) + "\n")
with open("title.txt","w+") as f:
    for i in title:
        f.write(str(i) + "\n")
driver.close()
fp.close()