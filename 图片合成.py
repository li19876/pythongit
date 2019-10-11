from PIL import Image
import easygui as e
import os
# 加载底图
def hec(bgimg,fimg,box):
    base_img = Image.open(bgimg)
    # 可以查看图片的size和mode，常见mode有RGB和RGBA，RGBA比RGB多了Alpha透明度
    # print base_img.size, base_img.mode
    # box = (334, 130, 640, 673)  # 底图上需要P掉的区域

    # 加载需要P上去的图片
    tmp_img = Image.open(fimg)
    fimgname = os.path.basename(fimg)
    print(fimgname)
    # 这里可以选择一块区域或者整张图片
    # region = tmp_img.crop((0,0,304,546)) #选择一块区域
    # 或者使用整张图片
    region = tmp_img

    # 使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
    # 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
    # 提前将图片进行缩放，以适应box区域大小
    # region = region.rotate(180) #对图片进行旋转
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    base_img.paste(region, box)
    # base_img.show() # 查看合成的图片
    base_img.save('./二维码/'+fimgname)  # 保存图片
if __name__=='__main__':
    fimg = e.diropenbox("选择二维码的文件夹")
    bgimg=e.fileopenbox("选择底图")
    filenames= os.walk(fimg)
    # print(fimg)
    files =[]
    filelist=[]
    for file in filenames:
        files =file
    for f in files[2]:
        filelist.append(files[0]+os.sep+f)
    box = (866,1732,1038,1901)
    for i in filelist:
        hec(bgimg,i,box)