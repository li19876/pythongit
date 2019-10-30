import requests
from lxml import etree
import time
import threading
from fake_useragent import UserAgent
import os
def getres(url):
    ua = UserAgent()
    # print("访问url",url)
    headers={"User-Agent": ua.random,
            "referer":"https://www.5atxt.com/0_841/",
             "Host":"www.5atxt.com"
             }
    while 1:
        res = requests.get(url,headers=headers)
        if res.status_code ==200:
        # print(res.text)
            return res
        else:
            pass


def getnext(res):
    pass
def parse(urllist,l,i):
    while l>0:
        lock=threading.Lock()
        burl = urllist.pop(0)
        while True:
            res = getres(burl[1])
            html = etree.HTML(res.text.encode(res.encoding).decode(res.apparent_encoding))
            content = html.xpath("string(//div[@id='content'])")
            # print(content)
            title = html.xpath('string(//div[@class="bookname"]/h1)')
            # print(title)
            if title:
                break
            else:
                time.sleep(2)
            # print(res.text)
        # print(title)
        # nexturl = "http://www.biquw.com"+html.xpath("//a[@class='next pager_next']/@href")
        lock.acquire()
        with open(str(burl[0])+".txt","w",encoding="utf-8") as f:
            f.write(title+"\n")
            f.write(content+"\n")
            print("线程{}写入了{}".format(i,title))
        lock.release()
        time.sleep(1.5)
# return {"content":content,"title":title}
def run(mulu="https://www.5atxt.com/0_841/"):
    # mulu = "http://www.biquw.com/book/86119/"
    res=getres(mulu)
    html = etree.HTML(res.text.encode(res.encoding).decode(res.apparent_encoding))
    bookname = html.xpath('//div[@id="info"]/h1/text()')[0]
    hreflist = html.xpath("//div[@id='list']/dl/dd/a/@href")[12:]
    # print(hreflist)
    urllist= []
    for href in hreflist:
        urllist.append("https://www.5atxt.com"+href)
    isExists = os.path.exists(bookname)
    if not isExists:
        os.mkdir(bookname)
        os.chdir(os.getcwd()+os.sep+bookname)
    else:
        os.chdir(os.getcwd() + os.sep + bookname)
    urllists = [[urllist.index(i),i] for i in urllist]
    print(urllists)
    print(bookname)
    th_list = []
    for i in range(1, 10):
        t = threading.Thread(target=parse, args=(urllists,len(urllists),i))
        print('*****线程%d开始启动...' % i)
        t.start()
        th_list.append(t)
        time.sleep(5)
    for t in th_list:
        t.join()
    package(bookname)

def package(bookname):
    list1=os.listdir(path=os.getcwd())
    # os.chdir(os.getcwd()+os.sep+bookname)
    with open(bookname + ".txt", "a", encoding="utf-8") as f: #打开总文件
        for i in range(len(list1)):
           with open(str(i)+".txt","r",encoding="utf-8") as fp:#打开每一个文件
                for s in fp:
                    # f.write("第"+str(i+1)+"章\n")
                    f.write(s)
           os.remove(os.getcwd()+os.sep+str(i)+".txt")
           print("写入一章,文件已删除")
    # print(len(list1))

if __name__ =="__main__":
    # bookname = '神道丹尊'
    # os.chdir(os.getcwd() + os.sep + bookname)
    # package(bookname)
    mulu = input("输入笔趣网书籍目录页链接:")
    if mulu == "":
        run()
    else:
        run(mulu)
