#coding=utf-8
"""执行所有用例"""
import logging
import unittest
import click
from Lid.BeautifulReport import BeautifulReport
from Config import  is_send
from Lid.e_mail import send_email,send_mail_yagmail
@click.command()
@click.option("--send", default="false", help="是否发送邮件")
def run_all(send):
    logging.info("====================== 测试开始 ======================")
    test_suite = unittest.defaultTestLoader.discover('./Test_Case', pattern='test*.py')
    result = BeautifulReport(test_suite)
    report_file =result.report(filename='中国人寿测试报告', description='自动化测试报告', log_path=".\Report") #log_path--报告文件写入路径
    logging.info("====================== 测试结束 ======================")
    if is_send or send == "True":
        # send_email(report_file)
        send_mail_yagmail(report_file)

if __name__ == '__main__':
    run_all()

