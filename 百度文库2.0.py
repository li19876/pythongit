# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 1：52
# @Author  : vk
# @Email   : vvvkkk1960@outlook.com


# 百度文库爬虫
# place
from tkinter import *
from tkinter import messagebox
import requests
import bs4
import json
import os
import pyperclip
import time
import re
import base64

# gui外壳部分
root = Tk()
session = requests.session()
root.title('vk--百度文库免费复制')

# 覆盖组件

lb = Label(root)
lb.place(relx=0.5, rely=0.6, anchor=N)

photo = PhotoImage(file='bg.gif')
Label(root, image=photo).pack()

Label(root, bg='yellow', fg='red', text='请输入文库文章网址：').place(relx=0.4, rely=0.5, anchor=E)

e1 = Entry(root)
e1.place(relx=0.42, rely=0.5, anchor=W)

# 获取剪切板内容,并写入
url = pyperclip.paste()
e1.insert(0, url)
var = IntVar()

v = IntVar()
v.set(1)
time.sleep(1)
top = Toplevel()
top.title('2.0新增版本特性')
top.attributes('-topmost', True)
top.attributes('-toolwindow', True)
Label1 = Label(top, fg='purple', bg='light blue',
               text='关注微信公众号:【vk智能】获取更多软件\n\n2.0版本特性:\n——————————\n1.新增支持所有文件格式\n\n2.请先复制网址再打开软件\n\n所有软件仅用来交流学习，切勿用于商业')
Label1.pack()
v = StringVar()
v.set('txt')
w = OptionMenu(root, v, 'txt', 'doc', 'ppt', 'xls')
w.place(relx=0.82, rely=0.5, anchor=E)


# 核心爬虫部分
# session保持登录信息
def get_url(url):
    try:
        return session.get(url).content.decode('gbk')

    except:
        messagebox.showwarning('FBI  WARNING!', '错误!')


def get_doc_id(url):
    url_list = url.split('/')
    for i in url_list:
        list2_ = i.split('.')
        doc_id = list2_[0]

    return doc_id


def get_type(soup):
    first = soup.find('h1', class_='reader_ab_test with-top-banner')
    b = first.find('b')
    type_all = b['class'][1]
    c = type_all.split('-')
    type = c[1]

    return type


def save(filename, result):
    with open(filename, 'w', encoding='utf-8')as f:
        f.write(result)
    return 2


def parse_txt(doc_id):
    content_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=' + doc_id
    content = get_url(content_url)
    dict1 = content.split('(')[1]
    dict1 = dict1.rstrip(')')
    dict2 = dict1.split(',')

    for i in dict2:
        i = i.split(':')
        if i[0] == '"md5sum"':
            md5 = i[1]
            md5 = md5.strip('"')
        if i[0] == '"totalPageNum"':
            pn = i[1]
            pn = pn.strip('"')

        if i[0] == '"rsign"':
            rsign = i[1]
            rsign = rsign.strip('"')

    content_url = 'https://wkretype.bdimg.com/retype/text/' + doc_id + '?rn=' + pn + md5 + '&type=txt' + '&rsign=' + rsign

    content = json.loads(get_url(content_url))
    result = ''

    for i in content:
        list2 = i['parags'][0]
        finall = list2['c'].replace('\r', '')

        result += finall
    return result


def parse_ppt(doc_id):
    content_url = 'https://wenku.baidu.com/browse/getbcsurl?doc_id=' + doc_id + '&pn=1&rn=99999&type=ppt'
    content = get_url(content_url)
    content = json.loads(content)

    https_list = []
    for i in content:
        https_list.append(i['zoom'])
    if not os.path.exists(doc_id):
        os.mkdir(doc_id)
    os.chdir(doc_id)
    a = 0
    for i in https_list:
        content = session.get(i).content
        a += 1

        with open('%d.jpg' % a, 'wb')as f:
            f.write(content)

    return 3


def parse_doc(content):
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    url_list = [addr.replace('\\\\\\/', '/') for addr in url_list]

    result = ''

    for url in url_list[:-4]:

        content = get_url(url)

        y = 0
        txtlist = re.findall('"c":"(.*?)".*?"y":(.*?),', content)
        for item in txtlist:

            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''

            result += n
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')

    return result


def get_title(soup):
    first = soup.find('span', class_='doc-header-title')
    title = first.text
    return title


def main():
    url = e1.get()
    content = get_url(url)
    soup = bs4.BeautifulSoup(content, 'html.parser')
    doc_id = get_doc_id(url)
    type = get_type(soup)
    title = get_title(soup)
    if type == 'txt':
        result = parse_txt(doc_id)
        save(title + '.txt', result)
        if 2:
            info = messagebox.showinfo('VK恭喜你复制成功', '已在于程序相同\n目录下保存为.txt的格式')
    elif type == 'ppt':
        result = parse_ppt(doc_id)
        if 3:
            info = messagebox.showinfo('VK恭喜你复制成功', '已在于程序相同\n目录下保存为图片的格式')
    elif type == 'doc' or type == 'xls':
        result = parse_doc(content)
        save(title + '.txt', result)
        if 2:
            info = messagebox.showinfo('VK恭喜你复制成功', '已在于程序相同\n目录下保存为.txt的格式')
    else:
        messagebox.showerror('FBI WARNING', '这个格式让俺怎么复制')


Button(root, text='搜索', command=main, padx=10, pady=10).place(relx=0.5, rely=0.7, anchor=N)

mainloop()

