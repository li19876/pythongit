from urllib import parse
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import re
keyword = "天津教育"
url = "https://www.tianyancha.com/search?key="+keyword
ua = UserAgent()
# 进入浏览器设置
options = webdriver.ChromeOptions()


# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent='+ua.random)
#禁止加载图片
# prefs = {"profile.managed_default_content_settings.images":2}
# options.add_experimental_option("prefs",prefs)

browser = webdriver.Chrome(chrome_options=options)
# browser.implicitly_wait(20)#隐式等待20s
browser.get(url)

wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="https://www.tianyancha.com/usercenter/modifyInfo"]')))
# print(browser.find_elements_by_xpath("/body"))
gsname = browser.find_elements(By.XPATH,"//div[@class='logo -w88']/img")
for i in gsname:
    gs = re.sub(r"<.+?>","",i.get_attribute("alt"))
    print(gs)





