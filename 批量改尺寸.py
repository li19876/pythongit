import easygui as e
import os
from PIL import Image
def hec(img):
    base_img = Image.open(img)
    imgname = os.path.basename(img)
    base_img=base_img.resize((3509,2481))  # A4
    base_img.save(imgname[:-4]+'_A4.jpg')
    # print(imgname[:-4]+'_A4.jpg')
    # base_img = base_img.resize((4962, 3509))  # A3
    # base_img.save(imgname[:-4] + '_A3.jpg')
    # print(imgname[:-4] + '_A3.jpg')
if __name__ == '__main__':
    fimg = e.diropenbox("选择图片文件夹")
    # bgimg=e.fileopenbox("选择底图")
    # print(os.path.dirname(bgimg))

    filenames= os.walk(fimg)
    # print(filenames)
    files =[]
    filelist=[]
    for file in filenames:
        # print(file)
        files =file
        break
    # print(files)
    for f in files[2]:
        filelist.append(files[0]+os.sep+f)
    resdir = fimg + os.sep + 'A4'
    isExists = os.path.exists(resdir)
    if not isExists:
        os.mkdir(resdir)
        os.chdir(resdir)
    else:
        os.chdir(resdir)
    # print(filelist)
    for i in filelist:
        hec(i)
        print(i)
