from Lid.Base_page import OpenSoftwareCase
from Config import url
from time import sleep
from Page_test.login_page import login_page
import unittest
class TestAsdf(unittest.TestCase):

    def setUp(self):
        print(0)
        self.driver = OpenSoftwareCase().open_browser(url)
    def tearDown(self):
        print(2)
        self.driver.quit()
