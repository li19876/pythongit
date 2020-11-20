import re

from lxml import etree
import requests
url = 'https://www.kq36.com/job/1520927'
headers= {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','referer':'https://www.kq36.com/job_list.asp?Job_ClassI_Id=2'}
res=requests.get(url,headers=headers)
html = etree.HTML(res.text)
text = html.xpath('string(//div[@class="job_info_div"])')
# print(text)
zhiwei = re.findall(r'职位类别[\s\S]+职位要求',text)[0]
zhiwei = re.sub('[\t\n\r\f\v]','',zhiwei)
zhiwei = re.sub(' ','',zhiwei)
zhiwei = re.sub('\.welfare.+3px}','',zhiwei)
zhiwei = zhiwei.replace('经验要求','；经验要求').replace('年龄要求','；年龄要求').replace('性别','；性别').replace('招聘人数','；招聘人数').replace('学历要求','；学历要求').replace('岗位性质','；岗位性质').replace('每周休息','；每周休息').replace('薪酬范围','；薪酬范围').replace('发布时间','；发布时间').replace('承诺月薪','；承诺月薪').replace('工作地点','；工作地点').replace('福利待遇','；福利待遇').replace('职位要求','')
zhiwei = {i.split("：")[0]:i.split("：")[1] for i in zhiwei.split('；')}
print(zhiwei)

contact = html.xpath('string(//div[@class="left"]/div/table[2])')
contact = re.sub('[\t\n\r\f\v]','',contact)
contact = re.sub('function.+hidden;}','',contact)
contact = re.sub('function.+地图/导航','',contact)
contact = re.sub('分享招聘海报.+click\(','',contact)
contact = re.sub(' ','',contact)
contact = re.sub('\xa0','',contact)
contact = contact.replace('QQ',';QQ').replace('电话号码',';电话号码').replace('举报单位','').replace('邮箱',';邮箱').replace('微信号',';微信号').replace('招聘网址',';招聘网址').replace('地　　址',';地址').replace('公交/地铁',';公交/地铁').replace('提示：收取费用或押金都可能有欺诈嫌疑，请举报，有效举报奖励200元','')
contact = {i.split("：")[0]:i.split("：")[1] for i in contact.split(';')}
print(contact)


