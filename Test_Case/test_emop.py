from Lid.Base_page import OpenSoftwareCase
from Config import emopurl
from time import sleep
import unittest
import unittest
from Lid.Base_page import OpenSoftwareCase
from Config import PFT
import allure
from Page_test.login_page import LoginEmop
import time
class PFTEmop(unittest.TestCase):
    """emop平台"""
    def setUp(self):
        print(0)
        self.driver = OpenSoftwareCase().open_browser(PFT)
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

"""emop登录"""
class LoginEMOP(PFTEmop):
    def testemop(self):
        """emop平台登录"""
        #1-登录账号
        LoginEmop(self.driver).loginemop("emopauto", "P@ssw0rd", "99")
        with allure.step('测试'):
            with open('./img/2021-08-30_21_38_46_截图一下.png', 'rb') as f:
                img = f.read()
            allure.attach(img,"大帅个")

        #3-查看网关列表数据
        # LoginEmop(self.driver).registeriot("UI自动化测试Python", "13703870305")
        #4-新建网关
        # LoginEmop(self.driver).seachiot()
        #5-新建设备
        time.sleep(3)
if __name__ == '__main__':
    LoginEMOP().testemop()

