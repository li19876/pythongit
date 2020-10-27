# coding=utf-8
"""
Author:song
"""
import os

import re
file='D:/360极速浏览器下载/tunshixingkong_wochixihongshi.txt/tunshixingkong.txt'
flag=1
filename = file.split('/')[-1]
newfilename='new_'+filename
path=os.path.dirname(file)
os.chdir(path)

with open(file,encoding='gb18030') as f:
    with open(newfilename,'a',encoding='utf-8') as n:
        for i in f:
            res=re.findall(r'\s第[\u4e00-\u9fa5]+章\s',i)
            if res:
                n.write(" 第{}章 ".format(str(flag))+i+'\n')
                flag+=1
            else:
                n.write(i+'\n')
