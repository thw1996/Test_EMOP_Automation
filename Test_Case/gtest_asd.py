from Lid.Base_page import OpenSoftwareCase
from Config import url
from time import sleep
from Page_test.login_page import login_page
import unittest
from Test_Case.Open_chrome import TestBaidu
from Lid.utils import retry



class TestLogin(TestBaidu):
    # @retry(times=2, wait_time=10)
    def testlogin(self):
        """打开百度的首页"""
        login_page(self.driver).user("ghf")
        sleep(1)
        # login_page(self.driver).ces()
        # yilist = ("css", "#su")
        self.driver.find_elements("css", "#su")[0].click()
        # ee = self.driver.find_elements("css", "#su")[0]
        print(self.driver.find_elements("class", " c-font-medium c-color-t opr-toplist1-subtitle"))

# class TestLoginT(TestBaidu):
#     img_path = 'img'
#     def testlogin3(self):
#         """打开百度的首页"""
#         print(1)
#         login_page(self.driver).user("dwada")
#         sleep(5)


if __name__ == '__main__':
    TestLogin().testlogin()