# coding=utf-8
import smtplib
from email.mime.text import MIMEText
def sendemail(to,title,content):
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

if __name__=='__main__':
    sendemail("1462063555@qq.com", "程序停止啦", "错误信息是:")