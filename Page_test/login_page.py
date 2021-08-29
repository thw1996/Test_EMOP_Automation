from Lid.Base_page import OpenSoftwareCase
from Config import url2
from Lid.Base_page import Auxiliary

"""emop平台登录"""
class LoginEmop(Auxiliary):
    """登录页面"""
    # 用户名
    user_loc = ("xpath", "//input[@placeholder='请输入用户名']")
    # 密码
    password_loc = ("xpath", "//input[@placeholder='请输入密码']")
    # 验证码
    Verification_loc = ("xpath", "//input[@placeholder='请输入图中算式结果']")
    # 登录按钮
    login_button_loc = ("xpath", "//div[@class='pop-login-form']//div[@class='pop-login-form-content']//div[@class='pop-login-form-content-button']//div//div")

    """平台管理页面"""
    # 平台管理
    Platform_loc =("xpath", "//div[@class='flex-layout__item mainmenuTitle']//span")
    # 网关管理
    gateway_loc = ("xpath", "//a[@class='active item']")
    # 数据点管理
    menubar_tag_loc = ("xpath", "//div[@id='menubar_tag']//a[@class='item']")
    # 版本管理
    menubar_version_loc = ("xpath", "//div[@id='menubar_version']//a[@class='item']")
    # 模板库管理
    menubar_template_loc = ("xpath", "//div[@id='menubar_template']//a[@class='item']")
    # 网关型号准入
    menubar_access_loc = ("xpath", "//div[@id='menubar_access']//a[@class='item']")



    #注册网关
    registeriot_loc =("id",'gateway-list_register')
    registeriot_name_loc =("xpath",'/html[1]/body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/input[1]')
    registeriot_SN_loc = ("css", 'div.sc-iRbamj.iKaaFv div:nth-child(1) div:nth-child(2) div:nth-child(2) span:nth-child(1) > input:nth-child(1)')
    registeriot_xinghao_loc =("xpath","/html[1]/body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/*[local-name()='svg'][1]")
    registeriot_noe_loc =("css",'div:nth-child(1) div:nth-child(3) div:nth-child(1) div.device-type-list.device-type-l > div.device-type-item:nth-child(1)')
    registeriot_two_loc =("css",'div:nth-child(1) div:nth-child(3) div:nth-child(2) div.device-type-list.device-type-l > div.device-type-item:nth-child(1)')
    registeriot_bt_loc = ("css",'div.flex-layout__column:nth-child(1) div.flex-layout__column.main-window:nth-child(2) div.flex-layout__column.gateway-container div.sc-cMljjf.VePhu:nth-child(4) div.register-gateway-wrapper div.sc-iRbamj.iKaaFv div:nth-child(1) div.footerBarReg:nth-child(5) div.footerBarCont > button.btn-normal')

    #查询网关新建设备
    device_iot_loc = ("css", 'div.sc-dxgOiQ.fajAsk')




    def user(self,user):
        self.input_element(self.user_loc,user)
        self.time(1)
    def password(self,password):
        self.input_element(self.password_loc,password)
        self.time(1)

    def Verifycode(self,vify):
        self.input_element(self.Verification_loc,vify)
        self.time(1)

    def loginbutton(self):
        self.click_element(self.login_button_loc)
        self.time(1)

    def fix(self):
        # 验证是否登录成功定位值
        fix_loc = ('xpath', '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/span[1]')
        fixoo = self.get_element_text(fix_loc)
        if fixoo != "平台管理":
            raise ("进入页面失败")

    # 动作层
    def loginemop(self,user,password,vify):
        self.user(user)
        self.password(password)
        self.Verifycode(vify)
        self.loginbutton()
        # self.fix()

    def registeriot(self,name,SN):
        self.click_element(self.registeriot_loc)
        self.input_element(self.registeriot_name_loc,name)
        self.input_element(self.registeriot_SN_loc, SN)
        self.click_element(self.registeriot_xinghao_loc)
        self.click_element(self.registeriot_noe_loc)
        self.click_element(self.registeriot_two_loc)
        self.time(3)
        self.click_element(self.registeriot_bt_loc)

    def seachiot(self):
        locs = self.driver.find_elements(self.device_iot_loc)
        print(locs)
        # fixoos = self.get_element_text(locs[1])
        # print(locs[1].text)
        # locs[0].click()


if __name__ == '__main__':
    driver = OpenSoftwareCase().open_browser(url2)
    LoginEmop(driver).loginemop("emopauto","P@ssw0rd","99")
