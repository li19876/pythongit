# -*- coding: utf-8 -*-
import scrapy
from biquge.items import BiqugeItem


class XiaoshuoSpider(scrapy.Spider):
	name = 'xiaoshuo'
	allowed_domains = ['www.bxwx.la','www.5atxt.com','www.jx.la','www.xiaoshuo240.cn','www.biquge.tw','www.xbiquge6.com']
	start_urls = ['https://www.5atxt.com/0_739/']

	def parse(self, response):
		bookname = response.xpath('//div[@id="info"]/h1/text()').get()
		hreflist = response.xpath("//div[@id='list']/dl/dd/a/@href").getall()[12:]
		urllist = []
		for href in hreflist:
			urllist.append(self.start_urls[0].split("/")[0] + "//" + self.start_urls[0].split("/")[2] + href)
		urllists = [[urllist.index(i), i] for i in urllist]

		for detail_url in urllists:
			url = detail_url[1]
			index = detail_url[0]
			items = {'bookname': bookname, 'index': index}
			yield scrapy.Request(url=url, callback=self.parse_detail, meta={'item': items})

	def parse_detail(self, response):
		print(response.meta['item'])
		item = BiqugeItem()
		item['title'] = response.xpath('string(//div[@class="bookname"]/h1)').get()
		content = response.xpath("//div[@id='content']/text()").extract()
		item['content'] = [i.strip() for i in content]
		item['index'] = response.meta['item']['index']
		item['bookname'] = response.meta['item']['bookname']
		yield item
