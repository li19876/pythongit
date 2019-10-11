# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BosSpider(CrawlSpider):
    name = 'bos'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=电话销售&page=1&ka=page-1']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.zhipin.com/c101010100/.+'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.zhipin.com/job_detail/.+'), follow=False,callback='parse_item'),
    )

    def parse_item(self, response):
        print(response.text)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
