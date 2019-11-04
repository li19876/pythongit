# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:22:02 2019
@author: Eric
"""
import requests
import re
from map_class import Address


def search_params(query, city, page=0):
	# 设置搜索的请求信息
	parameter = {
		'newmap': 1,
		'reqflag': 'pcmap',
		'biz': 1,
		'from': 'webmap',
		'da_par': 'direct',
		'pcevaname': 'pc4.1',
		'qt': 's',
		'da_src': 'searchBox.button',
		'wd': query,
		'wd2': '',
		'c': city,
		'src': 0,
		'pn': page,
		'sug': 0,
		'db': 0,
		# 'l': '11',
		'addr': 0,
		'biz_forward': {"scaler": 1, "styles": "pl"},
		'from': 'webmap',
		'auth': '2dZB4vFJNWZ8@9fL6v99La95@FOJRvx=uxHLLBNVLLztComRB199Ay1uVt1GgvPUDZYOYIZuEt2gz4yYxGccZcuVtPWv3GuRBtR9KxXwUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7ucvY1SGpuxxti0XEI=1mDLYClnDjnCENRRHN@Z@EBfiKKvCMuGllhIQT',
		'device_ratio': 1,
		'tn': 'B_NORMAL_MAP',
		'nn': page * 10,
		'ie': 'utf-8',
		't': '1566370557403'
	}
	return parameter


def reduce(stri):
	# 获取list结果
	stack = []
	str2 = ''
	flag = False
	for i in range(0, len(stri)):
		if stri[i] == '{':
			stack.append(stri[i])
			flag = True
		elif stri[i] == '}' and flag:
			stack.pop(-1)
		if flag:
			str2 = str2 + stri[i]
		if not len(stack) and flag:
			break
	if str2 == '':
		return False
	return str2


def search(query, city, findall=1, debug=False):
	"""findall=True 代表获取所有搜索结果
	   findall=False 代表获取第一页搜索结果
	"""
	try:
		# 访问网址
		url = 'http://map.baidu.com/'
		parameter = search_params(query, city, 0)
		response = requests.get(url, params=parameter)
		response.encoding = 'unicode_escape'  # 转码
		text = response.text.replace(' ', '')

		total = int(re.findall('total":(.*?),', text)[0])  # 获取结果数量

		if findall:
			max_page = (total // 10) + 1  # 结果最大页数
		else:
			max_page = 1

		results_list = []
		for i in range(1, max_page + 1):
			parameter = search_params(query, city, page=i - 1)
			response = requests.get(url, params=parameter)
			response.encoding = 'unicode_escape'
			text = response.text.replace(' ', '')
			xx1 = text.split(',"content":')
			xx2 = xx1[-1].split(',"current_city"')
			info = xx2[0]
			result = reduce(info)
			while result:
				results_list.append(result)
				info = info.replace(result, '')
				result = reduce(info)

		addresses = []
		for result in results_list:
			# print(result)
			address = Address()
			res=address.fill(result)
			addresses.append(res)
			if debug:
				print(address)
	except:
		return []
	return addresses


results_list = search('天津和平教育机构', 332)  # city为地区码，可以在百度搜索那里查看
for i in results_list:
	print(i)
# print(results_list)
