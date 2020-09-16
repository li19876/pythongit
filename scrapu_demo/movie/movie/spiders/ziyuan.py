# -*- coding: utf-8 -*-
import scrapy


class ZiyuanSpider(scrapy.Spider):
    name = 'ziyuan'
    allowed_domains = ['www.zuidazy2.net']
    start_urls = ['http://www.zuidazy2.net/?m=vod-type-id-1-pg-{}.html'.format(str(i)) for i in range(1,338)]
    # start_urls = ['http://www.zuidazy2.net/?m=vod-type-id-1.html']

    def parse(self, response):
        hreflist = response.xpath('//span[@class="xing_vb4"]/a/@href').getall()
        urllist = []
        for href in hreflist:
            urllist.append(self.start_urls[0].split("/")[0] + "//" + self.start_urls[0].split("/")[2] + href)
        for url in urllist:
            yield scrapy.Request(url=url, callback=self.download_detail)


    def download_detail(self,response):
        filename=response.request.url.split('-')[-1]
        with open('html/'+filename,'w',encoding='utf-8') as f:
            f.write(response.text)
            print('爬取一页:'+filename)
        # exit()

