# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class BiqugePipeline(object):
    def __init__(self):
        self.bookname =''
        # isExists = os.path.exists(self.bookname)
        # if not isExists:
        #     os.mkdir(self.bookname)
        #     os.chdir(os.getcwd() + os.sep + self.bookname)
        # else:
        #     os.chdir(os.getcwd() + os.sep + self.bookname)
        pass
    def process_item(self, item, spider):
        self.bookname= item['bookname']
        filename = str(item['index'])+'.txt'
        with open(filename,"w",encoding="utf-8") as f:
            print("创建文件:", filename)
            f.write("第{}章".format(str(item['index'])))
            f.write(item['title']+'\n')
            f.write(item['content']+'\n')
            # for i in item['content']:
            #     if i != "":
            #         f.write(i+'\n')
            print("{}写入完成".format(filename))

    def open_spider(self, spider):
        os.chdir(os.getcwd() + os.sep + '小说'+os.sep+'tmp')
        print("爬虫开始")

    def close_spider(self, spider):
        mark=[]
        bookname = self.bookname
        list1 = os.listdir(path=os.getcwd())
        # os.chdir(os.getcwd()+os.sep+bookname)
        with open("../"+bookname + ".txt", "a", encoding="utf-8") as f:  # 打开总文件
            for i in range(len(list1)):
                try:
                    with open(str(i) + ".txt", "r", encoding="utf-8") as fp:  # 打开每一个文件
                        for s in fp:
                            # f.write("第"+str(i+1)+"章\n")
                            f.write(s)
                    os.remove(os.getcwd() + os.sep + str(i) + ".txt")
                    print("写入一章,文件已删除")
                except Exception as e:
                    mark.append(str(e))
                    continue
                finally:
                    print("漏爬了{}章,错误信息如下{}\n".format(len(mark), mark))