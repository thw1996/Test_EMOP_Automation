#coding=utf-8
"""发送邮件"""
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Config import email_config
import yagmail

def send_email(report_file):
    # 1. 组装邮件正文
    msg = MIMEMultipart()
    body = MIMEText(email_config["body"], "plain", "utf-8")
    msg.attach(body)  # plain纯文本/html
    # 2. 组装邮件头
    msg["From"] = email_config["user"]
    msg["To"] = email_config["receiver"]
    msg["Subject"] = email_config["subject"]

    # 3. 添加附件
    attr = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    attr["Content-Type"] = "application/octet-stream"
    attr["Content-Disposition"] = "attachment; filename='测试报告.html'"
    msg.attach(attr)

    # 4. 连接smtp服务器并发送邮件
    smtp = smtplib.SMTP(email_config["server"])   # 连接smtp服务器
    smtp.login(msg["From"], "Li211211")  # 登录
    smtp.sendmail(msg["From"], msg["To"], msg.as_string())  # 发送
    logging.info("邮件发送完成")

def send_mail_yagmail(report):
    yag = yagmail.SMTP(user="1240898275@qq.com",password="bdzgfhkaxpqvjggb",host='smtp.qq.com')
    subject = "主题，自动化测试报告"
    contents = "正文，请查看附件"
    yag.send('super_u_t@163.com',subject,contents,report)
    logging.info("邮件发送完成")