from selenium import webdriver
import time , requests
from lxml import etree
from pyquery import PyQuery as pq
import re



url = 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU2NjM3Mzk0Nw==&scene=124&uin=NzgyNjg2NjQy&key=f3b89a09cde51f0ff750e88b7aeda5482f763af8714f732bf9acdd837c199954917c97109932116351bc48ca7acbd3f2f4169fe09a35e947584fbd0112cf5b0bbb3e422845cf2dfdca2be7ca4794e4f4&devicetype=Windows+7&version=62060833&lang=zh_CN&a8scene=7&pass_ticket=VpVE6boQ8Lc21W4SXq0kvNn4gHWUjO%2BYHRpsL7QM75VbcVcztJ6%2FkZW51cd0rkWa&winzoom=1'
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