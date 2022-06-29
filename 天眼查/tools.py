# codeing=utf-8
"""
Author:song
"""

import smtplib
from email.mime.text import MIMEText
""" 参数为浏览器直接复制的header字符串，返回处理好的headers字典 """
def make_header(header_str=''):
    headers = header_str.split('\n')
    # return headers
    headers_dict = {i.split(': ')[0].strip(): i.split(': ')[1].strip() for i in headers}
    return headers_dict


""" 参数为浏览器直接复制的cookie字符串，返回处理好的cookies字典 """
def make_cookie(cookie=''):
    cookies= {i.split("=")[0]:i.split("=")[1] for i in cookie.split(";")}
    return cookies


""""发送邮件，参数分别是收件人邮箱地址，邮件标题，邮件内容"""
def sendemail(to, title, content):
    msg_from = 'li.yansong@hzsr-media.com'  # 发送方邮箱
    # passwd = 'qbfifvahyylvfebj'  # 填入发送方邮箱的授权码
    passwd = 'li19980706..'  # 填入发送方邮箱的授权码
    msg_to = to  # 收件人邮箱

    subject = title  # 主题
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    try:
        s = smtplib.SMTP_SSL("smtp.sina.net", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except Exception as b:
        print(b)
        print("发送失败")
    finally:
        s.quit()

