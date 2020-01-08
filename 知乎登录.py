from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
def log():
    driver = webdriver.Chrome()
    url='https://www.zhihu.com/signin?next=%2F'
    driver.get(url)
    nowhandle = driver.current_window_handle  # 在这里得到当前窗口句柄
    print(nowhandle)
    logo = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div/form/div[1]/div[2]')
    WebDriverWait(driver, 10).until(lambda driver: logo.is_displayed())

    # 点击密码登录
    ActionChains(driver).click(logo).perform()
    time.sleep(1)
    # aalhandles = driver.window_handles  # 获取所有窗口句柄
    # driver.switch_to.window(aalhandles[-1])  # 这两步是在弹出窗口中进行的操作，证明我们确实进入了
    # shandle = driver.current_window_handle
    # print('窗口内句柄是:',shandle)
    # time.sleep(5)
    # iframe = driver.find_element_by_xpath(".//*[@id='ptlogin_iframe']")
    # driver.switch_to.frame(iframe)
    # qq =driver.find_element_by_xpath('//*[@id="qlogin_list"]/a[1]')
    # # WebDriverWait(driver, 10).until(lambda driver: qq.is_displayed())
    # ActionChains(driver).click(qq).perform()
    # time.sleep(3)
    # driver.switch_to.window(nowhandle)  # 返回到主窗口页面

    # # 输入账号
    driver.find_element_by_name('username').send_keys('18202610240')
    time.sleep(2)
    driver.find_element_by_name('password').send_keys('19980706..')
    time.sleep(2)
    login = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div/form/button')
    WebDriverWait(driver, 10).until(lambda driver: login.is_displayed())
    ActionChains(driver).click(login).perform()
    time.sleep(3)
    print(driver.get_cookies())
    time.sleep(30)

if __name__=='__main__':
    log()