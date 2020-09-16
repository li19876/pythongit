from lxml import etree
import requests
url1 = 'https://www.kaka1234.com/HTM/guochantaotu/list_6_5.html'
url2 = 'https://www.kaka1234.com/HTM/guochantaotu/list_6_6.html'

re = requests.get(url2)
re.encoding='gbk'
print(re.text)
print('*'* 80)
home_html = etree.HTML(re.text)
print(etree.tostring(home_html).decode())
url_next = home_html.xpath("//a[text()='下一页']//@href")
print(url_next)