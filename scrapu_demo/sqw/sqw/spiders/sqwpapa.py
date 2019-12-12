# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sqw.items import SqwItem
import re


class SqwpapaSpider(CrawlSpider):
	name = 'sqwpapa'
	allowed_domains = ['11467.com']
	start_urls = ['http://m.11467.com/shanghai/']

	rules = (
		Rule(LinkExtractor(allow=r'm.11467.com/shanghai/search/.+'), follow=True),
		# Rule(LinkExtractor(allow='m.11467.com/shanghai/search/.+'), follow=True),
		Rule(LinkExtractor(allow=r'm.11467.com/shanghai/co/.+htm'), callback='parse_item', follow=False),
	)

	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.Request(url, dont_filter= True)


	def parse_item(self, response):
		item = SqwItem()
		# 联系方式
		lxfs = response.xpath('//*[@id="contact"]/div/dl').get()
		# 地址
		addres = re.findall(r'地址：</dt><dd>(.+?)</dd>', lxfs)
		item['addres'] = addres[0] if addres else ''
		# 电话
		tel = re.findall(r'电话：</dt><dd><em>(.+?)</em></dd>', lxfs)
		item['tel'] = tel[0] if tel else ''
		# 经理
		manager = re.findall(r'经理：</dt><dd>(.+?)</dd>', lxfs)
		item['manager'] = manager[0] if manager else ''
		# 手机
		phone = re.findall(r'手机：</dt><dd><em>(.+?)</em></dd>', lxfs)
		item['phone'] = phone[0] if phone else ''
		# 传真
		chuanzhen = re.findall(r'传真号码：</dt><dd>(.+?)</dd>', lxfs)
		item['chuanzhen'] = chuanzhen[0] if chuanzhen else ''
		# 邮箱
		email = re.findall(r'邮件：</dt><dd>(.+?)</dd>', lxfs)
		item['email'] = email[0] if email else ''
		# 工商信息
		gsxx = response.xpath('//*[@id="gongshang"]/div/dl').get()
		# 公司名称
		gsname = re.findall(r'法人名称：</dt><dd>(.+?)</dd>', gsxx)
		item['gsname'] = self.check(gsname)
		# 经营范围
		jyfw = re.findall(r'经营范围：</dt><dd>(.+?)</dd>', gsxx)
		item['jyfw'] = self.check(jyfw)
		# 营业执照号码
		yyzz = re.findall(r'营业执照号码：</dt><dd>(.+?)</dd>', gsxx)
		item['yyzz'] = self.check(yyzz)
		# 发证机关
		fzjg = re.findall(r'发证机关：</dt><dd>(.+?)</dd>', gsxx)
		item['fzjg'] = self.check(fzjg)
		# 经营状态
		jyzt = re.findall(r'经营状态：</dt><dd>(.+?)</dd>', gsxx)
		item['jyzt'] = self.check(jyzt)
		# 法人代表
		frdb = re.findall(r'法人代表：</dt><dd>(.+?)</dd>', gsxx)
		item['frdb'] = self.check(frdb)
		# 成立时间
		clsj = re.findall(r'成立时间：</dt><dd>(.+?)</dd>', gsxx)
		item['clsj'] = self.check(clsj)
		# 职员人数
		zyrs = re.findall(r'职员人数：</dt><dd>(.+?)</dd>', gsxx)
		item['zyrs'] = self.check(zyrs)
		# 注册资本
		zczb = re.findall(r'注册资本：</dt><dd>(.+?)</dd>', gsxx)
		item['zczb'] = self.check(zczb)
		# 官方网站
		gfwz = re.findall(r'官方网站：</dt><dd>(.+?)</dd>', gsxx)
		item['gfwz'] = self.check(gfwz)
		# 所属分类
		ssfl = re.findall(r'所属分类：</dt><dd><a href=".+">(.+?)</a></dd>', gsxx)
		item['ssfl'] = self.check(ssfl)
		yield item

	@staticmethod
	def check(res):
		return res[0] if res else ''
