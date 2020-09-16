from selenium import webdriver

import time


def login():
    cookie="""RK=/2hJnxD8S1; ptcz=3cd088b9d9033403e5dde1b90f49b20b3c6b789be4023a28c9fc64f7081e8dd6; pgv_pvid=3614164490; pgv_pvi=8595558400; _ga=GA1.2.1122246799.1562208076; pt_235db4a7=uid=utOGnoApX5LEb3Iy70n/Ug&nid=1&vid=jfcICKfEyxsA5FfLth97MA&vn=1&pvn=1&sact=1562208075551&to_flag=0&pl=0KzaISwJA-wYoyVB1nkjpQ*pt*1562208075551; ied_qq=o1462063555; tvfe_boss_uuid=e080cb883b85c7ec; o_cookie=1462063555; XWINDEXGREY=0; gr_user_id=b640d631-6561-456f-b395-21e69c219191; pac_uid=1_1462063555; uin_cookie=o1462063555; UM_distinctid=1736a0b706ab6-004af30a1abcc1-43450521-1aeaa0-1736a0b706b4b4; nest_uin=3661300269; nest_uin.sig=4dkUbpTklukCVE6mKVI9ObHooA4; pgv_info=ssid=s7330145296; verifysession=h019383fb383acbcd7d39e3331eb3ed800b955fb58736705822eddab07c072bce55fb44d761dbe2180c; uin=o1462063555; UM_distinctid=1746d04e1665f2-00ad68049f0ee8-43450521-1aeaa0-1746d04e1675a3; pgv_si=s2395455488; skey=@vf2FSBcgV; _supWebp=1; CNZZDATA1272960370=966610873-1593744969-%7C1599720512; ilive_uin=3661300269; ilive_a2=a3afc8fb5c74a30af9aa3647316adf1a35270b7fb23685a57a896d71fd5451fff3b5656009819229d0ba67cb1460cc48271cbe73cfd0f0b3680907cc13cafa13c55a77ce3a4ac27b; ilive_tinyid=144115223792874674; ilive_uin=3661300269; ilive_a2=a3afc8fb5c74a30af9aa3647316adf1a35270b7fb23685a57a896d71fd5451fff3b5656009819229d0ba67cb1460cc48271cbe73cfd0f0b3680907cc13cafa13c55a77ce3a4ac27b; ilive_tinyid=144115223792874674; __logo=https%253A%252F%252Fnowpic.gtimg.com%252Fhy_personal%252F4376ae1e0cf0ccceb90048d103f221089fd7c2459d95518115ba2632c14dfdd831f936fc1a646e2359eefe89eb8f9be3%252F; __nick=%25E8%25BE%25BD%25E5%2590%2589%25E8%2582%25AF%25E5%25BE%25B7%25E5%259F%25BA"""
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
    url = 'https://tencentlive.qq.com/tliveadmin/managelive/program'
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--disable-gpu') # 无头模式
    # chrome_options.add_argument('--headless')
    chrome = webdriver.Chrome()
    chrome.set_window_size(1000, 800)
    # chrome.set_window_position(1700, 200)
    chrome.get("https://tencentlive.qq.com/tliveadmin/managelive/program")  # 先get一下后面才能加cookie
    # print('进来了')
    # chrome.get_screenshot_as_file('aaa.png')
    # print('截图了')
    for i in cookies:
        chrome.add_cookie({"name": i, "value": cookies[i]})
    chrome.get(url)
    # for i in cookies:
    #     chrome.add_cookie({"name": i, "value": cookies[i]})
    time.sleep(6000)
if __name__ == '__main__':
    login()