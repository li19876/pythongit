# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class SqwPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host="localhost", port=3306, user="root", password="li123456..", db='lys', charset="utf8")
        self.curosr = self.db.cursor()
    def process_item(self, item, spider):
        addres=item['addres']
        tel=item['tel']
        manager=item['manager']
        phone=item['phone']
        chuanzhen=item['chuanzhen']
        email=item['email']
        gsname=item['gsname']
        jyfw=item['jyfw']
        yyzz=item['yyzz']
        fzjg=item['fzjg']
        jyzt=item['jyzt']
        frdb=item['frdb']
        clsj=item['clsj']
        zyrs=item['zyrs']
        zczb=item['zczb']
        gfwz=item['gfwz']
        ssfl=item['ssfl']

        insert = """insert into sqwlist(addres,tel,manager,phone,chuanzhen,email,gsname,jyfw,yyzz,fzjg,jyzt,frdb, 
        clsj,zyrs,zczb,gfwz,ssfl) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
        '{}','{}')""".format(addres,tel,manager,phone,chuanzhen,email,gsname,jyfw,yyzz,fzjg,jyzt,frdb,
        clsj,zyrs,zczb,gfwz,ssfl)

        try:
            self.curosr.execute(insert)
            self.db.commit()
            print('写入了:',phone,chuanzhen,email,gsname,frdb)
        except Exception as e:
            self.db.rollback()
            print('错误:',str(e))
    def open_spider(self, spider):
        print("爬虫开始")

    def close_spider(self, spider):
        print('爬虫结束')