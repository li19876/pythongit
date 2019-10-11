import keyboard
from PIL import ImageGrab ,Image

import time
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '17219475'
API_KEY = 'wunGv6RtkjGbexAyh9yIKRjf'
SECRET_KEY = 'izG1oSuj1EBQ21A6YosKkLmv6aPcrXra'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)#配置百度接口

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()




while 1:
    print("等待中...")
    keyboard.wait(hotkey="ctrl+alt+a")

    while 1:
        image = ImageGrab.grabclipboard()
        if image:
            break
    image.save("cutimg.jpg")
    image = get_file_content('cutimg.jpg')
    print(image)
    """ 调用通用文字识别, 图片参数为本地图片 """
    res=client.basicAccurate(image)
    linenum =res["words_result_num"]
    for i in res["words_result"]:
        print(i["words"])
