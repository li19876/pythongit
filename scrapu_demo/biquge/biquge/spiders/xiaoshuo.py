# -*- coding: utf-8 -*-
import scrapy
from biquge.items import BiqugeItem


class XiaoshuoSpider(scrapy.Spider):
	name = 'xiaoshuo'
	allowed_domains = [
		'www.biquger.com','www.bxwx.la','www.5atxt.com','www.jx.la','www.xiaoshuo240.cn','www.biquge.tw','www.biquge.tv','www.xbiquge6.com','www.biquge.info','www.xinxs.la','www.siljy.com','www.paoshu8.com'
	]
	start_urls = ['http://www.biquger.com/biquge/22771/']

	def parse(self, response):
		bookname = response.xpath('//div[@id="info"]/h1/text()').get()
		hreflist = response.xpath("//div[@id='list']/dl/dd/a/@href").getall()[2850:2872]
		urllist = []
		for href in hreflist:
			urllist.append(href)
			# urllist.append(self.start_urls[0].split("/")[0] + "//" + self.start_urls[0].split("/")[2] + href)
			# urllist.append(self.start_urls[0] + href)
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
		item['content'] = response.xpath('string(//*[@id="booktext"])').get().replace('\u3000\u3000','\n')
		# print(content)
		# print(response.text)
		# item['content'] = [i.strip() for i in content]
		item['index'] = response.meta['item']['index']
		item['bookname'] = response.meta['item']['bookname']
		# print(item)
		yield item
