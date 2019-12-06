import requests
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()
url = "http://so.11467.com/cse/search?q={}&click=1&s=662286683871513660&nsid=3"


def getres(url):
	headers = {
		'user-agent': ua.random
	}
	response = requests.get(url, headers=headers)
	return response


def search(word):
	res = getres(url.format(word))
	html = etree.HTML(res.text.encode(res.encoding).decode(res.apparent_encoding))

	detail_url=html.xpath('//*[@id="results"]/div[1]/h3/a/@href')[0] if html.xpath('//*[@id="results"]/div[1]/h3/a/@href') else False

	if detail_url:
		detail_res = getres(detail_url)
		detail_html =etree.HTML(detail_res.text.encode(detail_res.encoding).decode(detail_res.apparent_encoding))
		phone = detail_html.xpath('//*[@id="logotel"]/text()')
		return phone if phone[0] else False
	return False



if __name__=='__main__':
	print(search("阿里巴巴"))