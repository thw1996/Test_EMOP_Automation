import unittest
from Lid.Base_page import OpenSoftwareCase

import time
# 中国人寿地址
class TestOpenchinalife(unittest.TestCase):
    def setUp(self):
        self.driver = OpenSoftwareCase().open_browser("https://www.w3school.com.cn/tiy/t.asp?f=js_prompt")
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def alert(self):
        time.sleep(5)
        alert = self.driver.switch_to.alert
        time.sleep(5)
        alert.send_keys("田惠文")
        alert_text = alert.text
        print(alert_text)
        time.sleep(5)
        #接收警告框
        alert.accept()
        #解散警告框
        # alert.dismiss()
if __name__ == '__main__':
    TestOpenchinalife().alert()


























