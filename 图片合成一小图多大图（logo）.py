from PIL import Image, ImageFont, ImageDraw
import easygui as e
import os
import time


# 加载底图
def hec(bgimg, fimg, box):
    base_img = Image.open(bgimg)
    resdir = os.path.dirname(fimg) + os.sep + os.path.basename(fimg)[:-4]
    isExists = os.path.exists(resdir)
    if not isExists:
        os.mkdir(resdir)
        os.chdir(resdir)
    else:
        os.chdir(resdir)
    # 可以查看图片的size和mode，常见mode有RGB和RGBA，RGBA比RGB多了Alpha透明度
    # print base_img.size, base_img.mode
    # box = (334, 130, 640, 673)  # 底图上需要P掉的区域

    # 加载需要P上去的图片
    tmp_img = Image.open(fimg)
    fimgname = os.path.basename(fimg)
    bgimgname = os.path.basename(bgimg)
    print(bgimgname)
    # 这里可以选择一块区域或者整张图片
    # region = tmp_img.crop((0,0,304,546)) #选择一块区域
    # 或者使用整张图片
    region = tmp_img
    # text = ''
    # for i in fimgname[:-4]:
    #     text += i + "  "
    # text = text[:-1]
    # 使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
    # 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
    # 提前将图片进行缩放，以适应box区域大小
    # region = region.rotate(180) #对图片进行旋转
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    base_img.paste(region, box)
    draw = ImageDraw.Draw(base_img)  # 修改图片
    # font = ImageFont.truetype('C:/Windows/Fonts/SourceHanSansK-Bold.ttf', 15)
    # draw.text((114, 327), text, fill=(0, 0, 0), font=font)  # 利用ImageDraw的内置函数，在图片上写入文字
    # base_img.show() # 查看合成的图片
    base_img.save(bgimgname)  # 保存图片


if __name__ == '__main__':
    bgimg = e.diropenbox("选择底图的文件夹")
    fimg=e.fileopenbox("选择logo")
    print(os.path.dirname(bgimg))
    filenames= os.walk(bgimg)
    # print(fimg)
    files =[]
    filelist=[]
    # 获取遍历后的文件元组
    for file in filenames:
        files =file
    # 拼接路径和文件名
    for f in files[2]:
        filelist.append(files[0]+os.sep+f)
    box = (400,400,600,600)
    print(filelist)
    start = time.time()
    for i in filelist:
        hec(i,fimg,box)
    end = time.time()
    print(end-start)

