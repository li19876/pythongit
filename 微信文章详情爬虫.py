import requests
from lxml import etree
from selenium import webdriver
url = 'http://mp.weixin.qq.com/s?__biz=MzU2NjM3Mzk0Nw==&mid=2247502431&idx=2&sn=b7c5f6d01fddfd8a64f8cd2cab5180b7&chksm=fcaff10bcbd8781d8f572e17befc45e8460f06c7a3c5d7472176cb381b5d9705f864d669bcd6&scene=38#wechat_redirect'
# Chromedriver
opt = webdriver.ChromeOptions()
# prefs = {'profile.default_content_setting_values': {'images': 2}}
# opt.add_experimental_option('prefs', prefs)#这两行是关闭图片加载
uas="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.884.400 QQBrowser/9.0.2524.400"
ua = 'user-agent=' + uas
opt.add_argument(ua)#设置headers
# # opt.add_argument('--headless')#此行打开无界面
driver = webdriver.Chrome(options=opt)
driver.get(url)