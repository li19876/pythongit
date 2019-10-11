from selenium import webdriver

import time



class login:

    def __init__(self):
        # self.path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe'
        # 进入浏览器设置
        # options = webdriver.ChromeOptions()
        # 更换头部
        # options.add_argument(
        #     'user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"')

        self.browser = webdriver.Chrome()


        url = 'https://tinder.com/app/recs'
        self.browser.get(url)
        time.sleep(20)
        #
        # self.browser.add_cookie(cookie1)
        # self.browser.add_cookie(cookie2)
        # self.browser.add_cookie(cookie3)
        # self.browser.add_cookie(cookie4)
        cookies = {'_ga':'GA1.2.1509980130.1566459270',
                   '_gid':'GA1.2.1848005561.1566459270',
                   'id':'22056e5626c0000a||t=1561522796|et=730|cs=002213fd48e6a5d76f878addd8',
                   'lang':'zh-Hans',
                   '_gat_gtag_UA_60214108_5':'1'
                   }
        # cookie = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        for i in cookies:
            self.browser.add_cookie({"name": i, "value": cookies[i]})

        self.browser.get(url)
        self.browser.implicitly_wait(20)
        self.browser.get(url)
        print(self.browser.get_cookies())

if __name__ == '__main__':
    login = login()