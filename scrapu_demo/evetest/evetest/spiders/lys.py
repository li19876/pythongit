# -*- coding: utf-8 -*-
import scrapy


class LysSpider(scrapy.Spider):
    name = 'lys'
    allowed_domains = ['hzsrwx.com']
    start_urls = ['http://hzsrwx.com/aa/python.html','http://hzsrwx.com/aa/python.html','http://hzsrwx.com/aa/python.html','http://hzsrwx.com/aa/python.html']

    def parse(self, response):
        print(response.text)
