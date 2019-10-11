# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class JianshuPipeline(object):
    def open_spider(self,spider):
        print("爬虫开始")
        with open("专题.csv", "a", encoding="utf-8-sig", newline="") as f:
            csv_write = csv.writer(f, dialect='excel')
            csv_write.writerow(["标题", "链接", "简介"])
    def process_item(self, item, spider):
        with open("专题.csv","a",encoding="utf-8-sig",newline="") as f:
            csv_write = csv.writer(f, dialect='excel')
            csv_write.writerow([item["title"], item["link"], item["desp"]])
            print(item)
    def stop_spider(self,spider):
        print("爬虫结束")