import requests
from lxml import etree
import time
import threading
from fake_useragent import UserAgent
import os

#获取网页资源
def getres(url):
	ua = UserAgent()
	# print("访问url",url)
	headers = {"User-Agent": ua.random,
			   'Connection': 'close',
			   "referer": url,
			   "Host": url.split("/")[2]
			   }
	mark=0
	while 1:
		if mark>=3:
			return False
		res = requests.get(url, headers=headers)
		if res.status_code == 200:
			# print(res.text)
			return res
		else:
			mark+=1
			print("访问失败,休息2s")
			time.sleep(2)
#解析result资源
def parse(urllist, i):
	while len(urllist) > 0:
		lock = threading.Lock()
		burl = urllist.pop(0)
		while True:
			res = getres(burl[1])
			if not res:
				urllist.append(burl)
				print("多次重试失败暂时放弃")
				break
			try:
				html = etree.HTML(res.text.encode(res.encoding).decode(res.apparent_encoding))
			except TypeError:
				urllist.append(burl)
				print("获取编码失败放弃")
				break
			content = html.xpath("//div[@class='contentbox']/text()")
			# print(content)
			title = html.xpath('string(//div[@class="h1title"]/h1)')
			# print(title)
			if title:
				break
			else:
				print("获取标题失败,休息2S")
				time.sleep(2)
		# lock.acquire()
		with open(str(burl[0]) + ".txt", "w", encoding="utf-8") as f:
			f.write(title + "\n")
			for s in content:
				f.write(s.strip()+"\n")
			print("线程{}写入了{},剩余{}章".format(i, title,len(urllist)))
		# lock.release()
		time.sleep(3)
	print("线程{}结束".format(i))

# return {"content":content,"title":title}
#主运行函数
def run(mulu="http://www.heiyan.org/wodelaoqianshengya/"):
	# mulu = "http://www.biquw.com/book/86119/"
	res = getres(mulu)
	html = etree.HTML(res.text.encode(res.encoding).decode(res.apparent_encoding))
	bookname = html.xpath('//div[@class="book_info"]/h1/text()')[0]
	hreflist = html.xpath("//div[@class='book_list']/ul/li/a/@href")[700:]
	# print(hreflist)
	urllist = []
	for href in hreflist:
		urllist.append(mulu.split("/")[0]+"//"+ mulu.split("/")[2]+ href)
	isExists = os.path.exists(bookname)
	if not isExists:
		os.mkdir(bookname)
		os.chdir(os.getcwd() + os.sep + bookname)
	else:
		os.chdir(os.getcwd() + os.sep + bookname)
	urllists = [[urllist.index(i), i] for i in urllist]
	print(urllists)
	print(bookname)
	th_list = []
	for i in range(1, 9):
		t = threading.Thread(target=parse, args=(urllists, i))
		print('*****线程%d开始启动...' % i)
		t.start()
		th_list.append(t)
		time.sleep(5)
	for t in th_list:
		t.join()
	package(bookname)


def package(bookname):
	list1 = os.listdir(path=os.getcwd())
	# os.chdir(os.getcwd()+os.sep+bookname)
	with open(bookname + ".txt", "a", encoding="utf-8") as f:  # 打开总文件
		for i in range(len(list1)):
			with open(str(i) + ".txt", "r", encoding="utf-8") as fp:  # 打开每一个文件
				for s in fp:
					# f.write("第"+str(i+1)+"章\n")
					f.write(s)
			os.remove(os.getcwd() + os.sep + str(i) + ".txt")
			print("写入一章,文件已删除")
	# print(len(list1))


if __name__ == "__main__":
	# bookname = '一剑独尊'
	# os.chdir(os.getcwd() + os.sep + bookname)
	# package(bookname)
	print("目前支持的网站有:\n","https://www.bxwx.la/\n", "https://www.5atxt.com\n","http://www.yuetutu.com http://www.xiaoshuo240.cn此行网站url列表前置可能不是12个\n","https://www.qu.la\n")
	mulu = input("请输入要下载的书籍目录页链接:")
	if mulu == "":
		run()
	else:
	  run(mulu)

	# urllist = [[0, 'https://www.bxwx.la/b/12/12588/7101302.html']]
	# parse(urllist,1)
