# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
import json
class BossPipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        j = json.loads(item)
        with open("jobs3.json","a") as f:
            f.write(j)

    def close_spider(self,spider):
        pass

