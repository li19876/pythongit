# -*- coding: utf-8 -*-
import scrapy
from jianshu.items import JianshuItem

class ZhuantiSpider(scrapy.Spider):
    name = 'zhuanti'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/c/a480500350e7?order_by=added_at&page='+str(i) for i in range(1,200)]

    def start_requests(self):
        yield scrapy.Request("http://b2b.huangye88.com/suzhou/")
    def parse(self, response):
        cont_list=response.xpath("//div[@class='content']")
        for a in cont_list:
            link = a.xpath(".//a/@href").get()
            title = a.xpath(".//a/text()").get()
            desp = a.xpath(".//p/text()").get().strip()
            item = JianshuItem()
            item["title"] = title
            item["link"]  = "https://www.jianshu.com"+link
            item["desp"]  = desp
            yield item