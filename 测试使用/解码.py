import os
from selenium import webdriver
import time



basedir = os.path.abspath(os.path.dirname(__file__))
def save_img(name):
    """界面截图"""
    driver = webdriver.Chrome()
    driver.get("https://emop-test.energymost.com/doorbell?path=/gateway&sysId=1&spDomain=sp1")
    title = name.replace("/", "").replace(":", "")
    file_path = os.path.join(basedir, "img", "{}{}.png".format('1', title))
    print(file_path)
    time.sleep(3)
    driver.get_screenshot_as_file(file_path)
    time.sleep(3)

if __name__ == '__main__':
    save_img('img')