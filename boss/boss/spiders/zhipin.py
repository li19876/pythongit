# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from boss.items import BossItem

class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/\w+~.html'), callback="parse_item",follow=False)
    )

    def parse_item(self, response):
        name = response.xpath("//div[@class='name']/h1/text()").get().strip()
        salary = response.xpath("//div[@class='name']/span/text()").get().strip()
        info = response.xpath("//div[@class='job-primary detail-box']//div[@class='info-primary']//p/text()").getall()
        city = info[0].strip()
        workYears = info[1].strip()
        education = info[2].strip()
        company = response.xpath("//div[@class='company-info']/a/text()").getall()[2].strip()
        boss = BossItem(name=name,salary=salary,jobCity=city,workYear=workYears,education=education,company=company)
        yield boss