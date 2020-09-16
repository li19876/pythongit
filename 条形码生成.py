# coding=utf-8
"""
Author:song
"""
import os
import barcode
import easygui as e
import time
from barcode.writer import ImageWriter


def create():
    path = e.fileopenbox("请选择要生成条形码的内容")
    filename = path.split("/")[-1][0:-4]
    isExists = os.path.exists(filename)
    if not isExists:
        os.mkdir(filename)
    else:
        pass
    f = open(path, "r")
    CODE128 = barcode.get_barcode_class('code128')  # 创建ean13格式的条形码格式对象
    for code in f:
        code2 = code.strip()
        ean = CODE128(code2, writer=ImageWriter())  # 创建条形码对象，内容为5901234123457
        fullname = ean.save(filename + os.sep + code2,
                            options={'module_height': 10.0, "write_text": False})  # 保存条形码图片，并返回保存路径。图片格式为png
        print(fullname)
    e.msgbox("生成条形码完成")


if __name__ == '__main__':
    # print(barcode.PROVIDED_BARCODES)
    start = time.time()
    create()
    end = time.time()
    print("用时:"+str(end-start))
