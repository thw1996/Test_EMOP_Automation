import os
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException,WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from Config import basedir
from Lid.logger import Log
# import win32api
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
# from Lid.BeautifulReport import BeautifulReport
from selenium.webdriver.chrome.options import Options



"""打开浏览器网页"""
class OpenSoftwareCase:
    def open_browser(self, url):
        # 无头模式
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        # chrome_options.add_argument('--disable-gpu')  # 处理 gpu bug
        # chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）
        # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 禁止加载图片
        # driver = webdriver.Chrome(options=chrome_options)
        # 有头模式
        driver = webdriver.Chrome()
        driver.get(url)
        Log().info("打开浏览器成功")
        # driver.maximize_window()
        sleep(5)
        return driver




class Auxiliary(object):
    """封装常规操作"""

    day = time.strftime("%Y-%m-%d_%H_%M_%S_", time.localtime(time.time()))
    def __init__(self, driver):
        self.driver = driver

    def save_img(self,name):
        """界面截图"""
        title = name.replace("/", "").replace(":", "")
        file_path = os.path.join(basedir, "img", "{}{}.png".format(self.day, title))
        self.driver.get_screenshot_as_file(file_path)

    def throw_error(error):
        """报错结束"""
        raise Exception(error)

    """此装饰器为吧截图加进报告里"""
    def find(self, element_loc):
        """
        查找元素如果定位失败报错截图
        """
        try:
            # 隐式等待
            # self.driver.implicitly_wait(60)
            # 显示等待
            element = WebDriverWait(self.driver, 20, 1.5).until(EC.presence_of_element_located(element_loc))
            Log().info("查找元素成功：{}".format(element_loc))
            return element
        except WebDriverException:
            Log().error("查找元素失败超过等待时常:{}".format(element_loc))
            try:
                element = self.driver.execute_script("arguments[0].scrollIntoView(false)", self.driver.find_element(*element_loc))
                Log().info("查找元素成功：{}".format(element_loc))
                return element
            except NoSuchElementException:
                self.save_img("查找元素失败")
                Log().error("查找元素失败:{}".format(element_loc))

    def is_element_exist(self, element_loc):
        """
        判断元素是否存在，存在返回真，不存在返回假
        """
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false)", self.driver.find_element(*element_loc))
            Log().info("元素存在:{}".format(element_loc))
            return True
        except NoSuchElementException:
            Log().info("元素不存在:{}".format(element_loc))
            return False

    def input_element(self, element_loc, text):
        """输入数据"""
        self.find(element_loc).send_keys(text)
        Log().info("输入成功:{}".format(text))

    def select_value(self,element_loc,value):
        """下拉框"""
        element = self.find(element_loc)
        Select(element).select_by_visible_text(value)
        Log().info("下拉框选择成功:{}".format(value))


    def click_element(self, element_loc):
        """鼠标点击"""
        self.find(element_loc).click()
        Log().info("点击成功:{}".format(element_loc))


    def double_click(self, element_loc):
        """双击"""
        element = self.find(element_loc)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, element_loc):
        """鼠标右键"""
        element = self.find(element_loc)
        ActionChains(self.driver).context_click(element).perform()

    def enter_key(self, element_loc):
        """回车键"""
        self.find(element_loc).submit()

    def F5(self):
        """F5刷新"""
        self.driver.refresh()

    def switch_iframe(self, element_loc):
        """切换Frame --待优化"""
        frame = self.find(element_loc)
        self.driver.swtch_to.frame(frame)

    def change_myFrame(self):
        """切换Frame"""
        self.driver.switch_to.frame(1)
        self.time(2)
        Log().info("切换myFrame成功")

    def switchwindows(self):
        """切换窗口"""
        nowhandle = self.driver.current_window_handle
        allhandles = self.driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                self.driver.switch_to.window(handle)


    def time(self, time):
        """等待时间"""
        sleep(time)

    def scroll(self):
        """滑动"""
        resolying = self.driver.get_window_size(windowHandle='current')
        right = resolying["width"]
        down = resolying["height"]
        js = "window.scrollTo({},{})".format(right.down)

    def scroll_select(self, element_loc):
        """滑动到元素位置"""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false)", self.driver.find_element(*element_loc))
            Log().info("找到元素:{}".format(element_loc))
        except NoSuchElementException:
            self.take_screen_shot("定位元素失败")
            Log().error("定位元素失败:{}".format(element_loc))
            raise

    def highlight(element):
        """高亮显示"""
        for i in range(150):
            if i % 2 == 0:
                driver.execute_script("arguments[0].style.border='4px solid red'", element)
            else:
                driver.execute_script("arguments[0].style.border=''", element)


    def get_element_attribute(self,element,attribute):
        """获取元素属性值"""
        try:
            text = self.find(element).get_attribute(attribute)
            Log().info("当前{}属性值:{}".format(attribute,text))
            return text
        except BaseException:
            text = self.find(element).text
            Log().info("当前text属性值:{}".format(text))
            return text

    def get_element_text(self,element):
        """获取原元素text"""
        text = self.find(element).text
        Log().info("当前text属性值:{}".format(text))
        return text




if __name__ == '__main__':
    driver = OpenSoftwareCase().open_browser("https://pinnacle-sss-zhj-sit-dr.ikpl.cloud.cn.hsbc/")
    resolving = driver.get_window_size(windowHandle='current')
    right = resolving["width"]
    down = resolving["height"]
    js = "window.scrollTo({},{})".format(right, down)
    driver.execute_script(js)














