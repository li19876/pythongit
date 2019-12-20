import os, math
from PIL import Image,ImageDraw
import requests
import sys
def get_headimg(url='http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJGv4zdYM3t0ZsZrj2Fjavcwzm3Rib6uvpbNkyy5LOKbEsVUgZFiauAXiaaoq6waknyHuVrtCsmSyRZQ/132'):
    res=requests.get(url)
    if res.status_code == 200:
        try:
            with open(url.split('/')[-2]+'.png','wb') as f:
                f.write(res.content)
                return url.split('/')[-2]+'.png'
        except Exception as e:
            print (str(e))
            exit()

def hec(bgimg, fimg):
    box = (90, 127, 189, 226)
    # 加载底图
    base_img = Image.open(bgimg).convert("RGBA")
    # 加载透明图
    touming = Image.open('touming.png').convert("RGBA")
    # 加载需要p上的图
    tmp_img = Image.open(fimg).convert("RGBA")
    fimgname = os.path.basename(fimg)
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
    touming.paste(region, box)
    draw = ImageDraw.Draw(touming)  # 修改图片
    touming.save('datouming.png')
    datouming = Image.open("datouming.png").convert('RGBA')
    final2 = Image.new("RGBA", base_img.size)

    final2 = Image.alpha_composite(final2,base_img)

    final2 = Image.alpha_composite(final2, datouming)

    # final2.show()

    final2.save(fimg)




    # font = ImageFont.truetype('C:/Windows/Fonts/SourceHanSansK-Bold.ttf', 15)
    # draw.text((114, 327), text, fill=(0, 0, 0), font=font)  # 利用ImageDraw的内置函数，在图片上写入文字
    # base_img.show() # 查看合成的图片
    # base_img.save('result.png')  # 保存图片


def circle_new(headimg_name):
    ima = Image.open(headimg_name).convert("RGBA")

    size = ima.size

    r2 = min(size[0], size[1])

    if size[0] != size[1]:

        ima = ima.resize((r2, r2), Image.ANTIALIAS)

    circle = Image.new('L', (r2, r2), 0)

    draw = ImageDraw.Draw(circle)

    draw.ellipse((0, 0, r2, r2), fill=255)

    alpha = Image.new('L', (r2, r2), 255)

    alpha.paste(circle, (0, 0))

    ima.putalpha(alpha)

    ima.save(headimg_name)


if __name__=='__main__':
    head = sys.argv[1]
    if head:
        headimg = get_headimg(head)
        circle_new(headimg)
        # box = (90, 127, 189, 226)
        hec('dt.png',headimg)
    else:
        print ("参数为空!")
        exit()
