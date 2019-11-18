import easygui as e
import os


fimg = e.diropenbox("选择二维码的文件夹")
filenames= os.walk(fimg)
files =[]
filelist=[]
for file in filenames:
    files =file
for f in files[2]:
    print(f[:-4])
# print(filelist)
