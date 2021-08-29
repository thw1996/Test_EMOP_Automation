from Lid.Base_page import OpenSoftwareCase
from Config import url2
from Lid.Base_page import Auxiliary

"""emop平台登录"""
class EmopGateway(Auxiliary):

    """网关管理页面"""
    # 客户名
    title_name_loc = ("xpath", "//div[@class='title customerName']")
    # 物理网关
    gateway_loc = ("xpath", "//a[@class='sc-elJkPf aWDkX']")
    # 虚拟网关
    emdc_loc = ("xpath", "//a[@class='sc-elJkPf kUuBuJ']")
    # 注册网关
    registeriot_loc =("id",'gateway-list_register')
    # 绑定已导入SN
    gateway_list_bind_loc = ("xpath", "//span[@id='gateway-list_bind-SN']")
    # 网关-名称按钮--多个网关
    gateway_name_loc = ("class", "sc-jAaTju gWRLuW")
    # 设备管理-- 多个
    device_btn_loc = ("id", "gateway-list_device")
    # ... 网关操作--多个
    gateway_act_loc = ("class", "icon-more")


    """注册网关页面"""
    # 网关名称
    gate_name_loc = ("xpath", "//input[@placeholder='请输入网关名称']")
    # SN（序列号）
    gate_sn_loc = ("xpath", "//input[@placeholder='请输入SN号']")
    # ICCID(选填)
    gate_iccid_loc = ("xpath", "//input[@placeholder='20位ICCID号']")
    # 厂商/型号
    Manufacturer_model_loc = ("xpath", "//div[@class='arrow-container']//*[local-name()='svg']")
    # 注册
    register_disable_loc = ("xpath", "//button[@class='btn-disable']")
    register_normal_loc = ("xpath", "//button[@class='btn-normal']")
    # 取消
    cancel__loc = ("xpath", "//button[@class='btn-normal-cancle']")



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
