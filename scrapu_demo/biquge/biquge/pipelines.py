# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class BiqugePipeline(object):
    def __init__(self):
        self.bookname =''

    def process_item(self, item, spider):
        index = item['index']
        if index ==0:
            bookname = item['bookname']
            self.bookname=bookname
            isExists = os.path.exists(bookname)
            if not isExists:
                os.mkdir(bookname)
                os.chdir(os.getcwd() + os.sep + bookname)
            else:
                os.chdir(os.getcwd() + os.sep + bookname)
        with open(str(index)+'.txt',"w",encoding="utf-8") as f:
            f.write(item['title']+'\n')
            for i in item['content']:
                if i != "":
                    f.write(i+'\n')

    def open_spider(self, spider):
        print("爬虫开始")

    def close_spider(self, spider):
        mark=0
        bookname = self.bookname
        list1 = os.listdir(path=os.getcwd())
        # os.chdir(os.getcwd()+os.sep+bookname)
        with open(bookname + ".txt", "a", encoding="utf-8") as f:  # 打开总文件
            for i in range(len(list1)):
                try:
                    with open(str(i) + ".txt", "r", encoding="utf-8") as fp:  # 打开每一个文件
                        for s in fp:
                            # f.write("第"+str(i+1)+"章\n")
                            f.write(s)
                    os.remove(os.getcwd() + os.sep + str(i) + ".txt")
                    print("写入一章,文件已删除")
                except:
                    mark+=1
                    continue
                finally:
                    print("漏爬了{}章".format(mark))