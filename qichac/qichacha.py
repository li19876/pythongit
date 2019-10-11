import re
import requests
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
def urlopenss(url):
	header={
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
		'Cookie':'_uab_collina=152464650553728421554052; zg_did=%7B%22did%22%3A%20%22162fc032b755dc-04e38756879671-6b1b1279-15f900-162fc032b76872%22%7D; _umdata=D4FF2234C2D4BB9084E5EDC630BEC0F04F43532920CEB85FADA5D8A2454FF22492FFF48B87575604CD43AD3E795C914C56051A4866DB8A847B3B5374BC2C81BB; UM_distinctid=16a0b8678c34c8-0d496ee3589b6b-454c092b-15f900-16a0b8678c4736; acw_tc=2a51048715599183023067532ef6dd18381dc451063fad1b59d0a9b91a; QCCSESSID=u1u7n9sq7dp591nt9nllqe0sp0; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1560504071,1560742016,1560747438,1560749429; CNZZDATA1254842228=882415236-1554967313-%7C1560751033; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201560749428835%2C%22updated%22%3A%201560751558145%2C%22info%22%3A%201560492892343%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22815c37b1963e2b7252cc310087050e85%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1560751558',
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.9',
		'Connection':'keep-alive'
		}
	req=requests.get(url,headers=header)
	#html = req.read()
	return req
def main(file="./kehu.txt"):
	gongsi = []
	chrome = webdriver.Chrome()
	with open(file,"r",encoding="utf-8") as f:
		for i in f:
			gongsi.append(i[:-1])
	ziliao = []
	with open("xxx.txt","at",encoding="utf-8") as f:	
		for i in gongsi:
			try:
				selector=chrome.get("http://www.qichacha.com/search?key="+i)
				if chrome.find_element("id","qrcodeLogin"):
					time.sleep(5)
				for handle in chrome.window_handles:#方法二，始终获得当前最后的窗口，所以多要多次使用
					chrome.switch_to_window(handle)
			except:
				pass
				# print(reason)
				# continue
			# selector2= etree.HTML(selector.text)
			try:
				name = chrome.find_element(By.XPATH,'//tbody[@id="search-result"]/tr[1]/td[3]/p[1]/a')
				name = name.get_attribute("innerText")
			except:
				continue
			# name = selector2.xpath('//tbody[@id="search-result"]/tr[1]/td[3]/p[1]/a/text()')
			if name != []:
				print("name是",name,end=' ')
				# number = selector2.xpath('//tbody[@id="search-result"]/tr[1]/td[3]/p[2]/span/text()')
				number = chrome.find_element(By.XPATH,'//tbody[@id="search-result"]/tr[1]/td[3]/p[2]/span')
				number = number.get_attribute("innerText")
				print("电话是",number,end=' ')
				ziliao=i+" "+name+" "+number+"\n"
				f.write(ziliao)
				print("写入成功")
			else:
				# gsm=selector2.xpath('//a[@class="btn-wx"]/@href/text()')
				pass
			time.sleep(5)
			print("休息5s")
			
main()
