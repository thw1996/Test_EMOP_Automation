
import os
import time

"""路径配置"""
basedir = os.path.abspath(os.path.dirname(__file__))
"""获取当前时间"""
date_time = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
# is_send = True      # 发送邮件
is_send = False     # 不发送邮件
url = 'http://www.baidu.com'
url1 = "http://192.168.171.58:8085/RecordHF/"
url2 = "https://testrec.sinosofter.com.cn/GSEasyRecord/"
emopurl = "https://emop-test.energymost.com/doorbell?path=/gateway&sysId=1&spDomain=sp1"
SUPurl = "https://atlas-sup.energymost.com/#/blackList"
PFT = "https://emop-pft.energymost.com/doorbell?path=/gateway&sysId=1&spDomain=emopauto"

"""邮件配置"""
email_config = {
    "server": "smtp.exmail.qq.com",
    "user": "1240898275@qq.com",
    "password": "suiyuerxing",
    "body": "hi, 测试报告请查看附件",
    "subject": "APP测试报告",
    "receiver": "627617481@qq.com"
}

"""数据库数据"""
sit_db_config ={
    "host": "hk120150802.hk.hsbc" ,#jdbc:postgresql://postgres:5432/dualrec
    "port":"25011",
    "user":"pinhkdal",
    "password":"fmfsAdLnqo",
    "database":"dhkpinpol"
}
dev_db_config = {
    "host": "hk120150802.hc.cloud.hk.hsbc",  # jdbc:postgresql://postgres:5432/dualrec
    "port": "25011",
    "user": "pinhkdal",
    "password": "abcd1234",
    "database": "uhkpin01"
}
db_config = {
    "host": "hk120150802.hc.cloud.hk.hsbc",  # jdbc:postgresql://postgres:5432/dualrec
    "port": 25011,
    "user": "pinhkdal",
    "password": "abcd1234",
    "database": "uhkpin01"
}

upload_status_sql = "select interactive from dualrec.lscont where businum = '{}'"



