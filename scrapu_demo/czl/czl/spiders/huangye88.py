# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from czl.items import CzlItem

class Huangye88Spider(CrawlSpider):
    name = 'huangye899'
    allowed_domains = ['b2b.huangye88.com']
    start_urls = ['http://b2b.huangye88.com/tianjin/']

    rules = (
        Rule(LinkExtractor(allow=r'http://b2b.huangye88.com/tianjin/.+/'),follow=True),
        Rule(LinkExtractor(allow=r'http://b2b.huangye88.com/qiye.+/'), follow=False,callback="parse_item"),
    )
    def parse_item(self, response):
        gsname = response.xpath("//div[@class='title']/h1[@class='big']/text()").get()
        if gsname:#判断如果页面样式为样式1获取方式
            gsname=gsname.strip()
            lxrname = response.xpath("//ul[@class='l-txt none'][1]/li[1]/a/text()").get().strip()
            phone = response.xpath("//ul[@class='l-txt none'][1]/li[4]/text()").get().strip()
            fenlei = response.xpath("//div[@class='bread']/a/text()").getall()
            fenlei = ">".join(fenlei)
        else:
            gsname = response.xpath("//div[@class='header']/div/p/text()").get().strip()
            phone = response.xpath("//li[@class='iphone-number']/text()").get().strip()
            lxrname = response.xpath("//div[@class='fangshi']/ul/li[1]/em/text()").get().strip()
            fenlei = response.xpath("//div[@class='mianbaoxie']/a/text()").getall()
            fenlei = ">".join(fenlei)
        item = CzlItem()
        item["gsname"] = gsname
        item["frname"] = lxrname
        item["phone"] = phone
        item["trade"] = fenlei
        yield item