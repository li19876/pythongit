# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time
class CzlPipeline(object):
    def open_spider(self,spider):
        print("爬虫开始")
        self.db = pymysql.connect(host="localhost",port=3306,user="root",password="li123456..",db='lys',charset="utf8")
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        sql = """
            insert into customer(city,trade,frname,gsname,phone,timestamp) values ('{}','{}','{}','{}','{}','{}')
        """.format(item["gsname"][0:2],item["trade"],item["frname"],item["gsname"],item["phone"],int(time.time()))
        try:
            print("开始写入")
            self.cursor.execute(sql)
            res=self.db.commit()

            print(res)
        except:
            self.db.rollback()

    def stop_spider(self,spider):
        self.db.close()
        print("爬虫结束")