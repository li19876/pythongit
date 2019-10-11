# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CzlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gsname = scrapy.Field()
    frname = scrapy.Field()
    phone = scrapy.Field()
    trade = scrapy.Field()
