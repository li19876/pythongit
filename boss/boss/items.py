# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    name = scrapy.Field()
    salary = scrapy.Field()
    jobCity = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    company = scrapy.Field()
