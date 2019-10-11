# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class HhhPipeline(object):
    def open_spider(self, spider):
        print("爬虫开始")
        with open("data.csv", "a", encoding="utf-8", newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['公司名', '联系人', '联系方式', '公司所属类别'])

    def process_item(self, item, spider):
        with open("data.csv", "a", encoding="utf-8", newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([item["gsname"], item["lxrname"], item["phone"], item["fenlei"]])
        print(item)

    def stop_spider(self, spider):
        print("爬虫结束")