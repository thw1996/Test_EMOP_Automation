from Lid.logger import Log
from Lid.Base_page import Auxiliary

class HomePage(Auxiliary):
    #质检管理
    quality_management_loc = ("xpath","//*[text()='质检管理']")
    #质检审核
    audit_loc = ("xpath","//*[text()='质检审核']")
    #任务分派
    allot_loc = ("xpath","//*[text()='任务分派']")
    #释放任务
    release_loc = ("xpath","//*[text()='释放任务']")
    #双录视频查询
    video_query_loc = ("xpath","//*[text()='双录视频查询']")
    #基础配置
    basic_configuration_loc = ("xpath","//*[text()='基础配置']")
    #机构管理
    institutional_management_loc = ("xpath","//*[text()='机构管理']")
    #产品管理
    productmanagement_loc = ("xpath","//*[text()='产品管理']")
    #话术管理
    discourse_management_loc = ("xpath","//*[text()='话术管理']")
    #话术模板
    word_template_loc = ("xpath","//*[text()='话术模板']")
    #系统管理
    system_managment_loc = ("xpath","//*[text()='系统管理']")
    #角色
    character_loc = ("xpath","//*[text()='角色']")
    #日志审计管理
    log_audit_loc = ("xpath","//*[text()='日志审计管理']")
    #登录日志管理
    log_log_loc = ("xpath","//*[text()='登录日志管理']")
    #操作日志管理
    operation_log_loc = ("xpath","//*[text()='操作日志管理']")
    #质检管理
    def quality(self):
        self.click_element(self.quality_management_loc)
        self.time(2)
        Log().info("点击质检管理成功")

    #质检审核
    def audit(self):
        self.click_element(self.audit_loc)
        self.time(2)
        Log().info("点击质检审核成功")
    #任务分派
    def allot(self):
        self.click_element(self.allot_loc)
        self.time(2)
        Log().info("点击任务分派成功")

    #释放任务
    def release(self):
        self.click_element(self.release_loc)
        self.time(2)
        Log().info("点击释放任务成功")
    #双录视频
    def videoquery(self):
        self.click_element(self.video_query_loc)
        self.time(2)
        Log().info("点击双录视频成功")

    #基础配置
    def basic(self):
        self.click_element(self.basic_configuration_loc)
        self.time(2)
        Log().info("点击基础配置成功")
    #机构管理
    def institutional(self):
        self.basic()
        self.click_element(self.institutional_management_loc)
        self.time(2)
        Log().info("点击机构管理成功")

    #产品管理
    def product(self):
        self.basic()
        self.click_element(self.productmanagement_loc)
        self.time(2)
        Log().info("点击产品管理成功")

    #话术管理
    def discourse(self):
        self.basic()
        self.click_element(self.discourse_management_loc)
        self.time(2)
        Log().info("点击话术管理成功")

    #话术模板
    def template(self):
        self.basic()
        self.click_element(self.word_template_loc)
        self.time(2)
        Log().info("点击话术模板成功")

    #系统管理
    def system(self):
        self.basic()
        self.click_element(self.system_managment_loc)
        self.time(2)
        Log().info("点击机构管理成功")

    #角色
    def character(self):
        self.basic()
        self.click_element(self.character_loc)
        self.time(2)
        Log().info("点击产品管理成功")

    #日志审计管理
    def logaudit(self):
        self.basic()
        self.click_element(self.log_audit_loc)
        self.time(2)
        Log().info("点击机构管理成功")

    #登录日志管理
    def logindit(self):
        self.basic()
        self.click_element(self.log_audit_loc)
        self.time(2)
        Log().info("点击机构管理成功")

    #操作日志管理
    def operationlog(self):
        self.basic()
        self.click_element(self.operation_log_loc)
        self.time(2)
        Log().info("点击机构管理成功")

class HomePage2(Auxiliary):
    # 账号
    user_loc = ("id", "userNo")
    # 登录
    audit_loc = ("id", "btn")
    # 视频管理
    video_Administration = ("xpath", "//div/span[text()='视频管理222']")
    # video_Administration = ("css selector", "#menu .panel:nth-of-type(1) li:nth-of-type(2) .tree-title")
    # 切换iframe
    myFrame = ("xpath", '//*[@id="_mainframe"]/div[2]/div[2]/div/iframe')
    # 客户号
    kehuhao = ("css selector", "body #q_frm:nth-of-type(1) tr:nth-of-type(1) .style_td:nth-child(2) [autocomplete]")
    # 员工号
    yuangonghao = ("css selector", "body tr:nth-of-type(1) .style_td:nth-child(4) [autocomplete]")
    # 记录状态
    jiluzhuangtai = ("css selector", "body tr:nth-of-type(1) .style_td:nth-child(6) [autocomplete]")
    jiluzhuangtai2 = ("css selector", "body .combo-p:nth-child(5) .panel-body-noheader div:nth-of-type(7)")
    # 交易流水号
    jiaoyiliushuihao = ("css selector", "body #q_frm:nth-of-type(2) [autocomplete]")
    # 业务类型
    yewuleixing = ("css selector", "body tr:nth-of-type(2) .style_td:nth-child(2) [icon-index]")
    yewuleixing2 = ("css selector", "body > .panel.combo-p:nth-child(6) > div:nth-child(1)")
    # 录制开始日期
    luzhiriqi = ("css selector", "body tr:nth-of-type(3) .style_td:nth-child(2) [autocomplete]")
    luzhiriqi2 = ("css selector", "[datebox-button-index='0']")
    # 员工网点缩写
    yuangongwangdiansuxie = ("css selector", "body tr:nth-of-type(4) .style_td:nth-child(4) [autocomplete]")

    def video_Administration_c(self):
        self.click_element(self.video_Administration)
        self.time(2)
        Log().info("点击视频管理成功")

    def change_myFrame(self):
        self.driver.switch_to.frame(1)
        self.time(2)
        Log().info("切换myFrame成功")

    def yuangong_input(self, a):
        self.input_element(self.yuangonghao, a)
        self.time(2)
        Log().info("员工号输入成功")

    def work_folw(self):
        # 调用流程
        pass

    def zhanghao_inpu(self):
        self.input_element(self.yuangonghao, a)
        self.time(2)
        Log().info("账号输入成功")

#中国人寿主界面
class MainPage(Auxiliary):
    # -------------------------主页面---------------------------
    #质检审核
    quality_management_loc = ("xpath","//*[text()='质检审核']")

    def qualitymanagement(self):
        self.click_element(self.quality_management_loc)
        Log().info("质检审核点击成功")

    #---------------------------质检审核页面-------------------------
    #保单号块
    contno_loc = ("xpath", '//*[@id="datagrid-row-r7-2-0"]/td[2]')
    def contno(self):
        self.change_myFrame()
        self.click_element(self.contno_loc)
        Log().info("进入质检管理页面")
    # --------------------------质检管理页面--------------------------
    """
    质检节点检查
    """
    #质检结论
    ipt_conclusion_loc = ("id",'ccf47b709214684be7a21a9c13724206f7')
    #质检问题
    inspection_pbc_loc =("xpath",'//*[@id="datagrid-row-r9-2-0"]/td[4]/div/span[1]/span/a')
    inspection_pbc_loc2 =("xpath","//*[text()='0-填写类']")
    inspection_pbc_loc3 =("xpath",'//*[@id="datagrid-row-r9-2-0"]/td[4]/div/span[2]/span/a')
    inspection_pbc_loc4 =("xpath","//*[text()='DSAD']")
    #操作保存
    save_button_loc = ("xpath", '//*[@id="datagrid-row-r9-2-0"]/td[5]/div/input')

    """
    其他问题
    """
    #质检结论
    conclusion_loc =("id","cc1")
    #质检问题
    question_loc = ("id","cc")
    #操作保存
    save_operation_loc =("id","b5")
    #弹框
    elastic_loc = ("xpath", "/html/body/div[9]/div[2]/div[4]/a/span/span")



    """
    待整改的质检节点
    """
    #整体质检结论
    Overall_conclusion_loc = ("xpath",'//*[@id="t_frm"]/table/tbody/tr[1]/td[2]/span/span/span/a')
    Overall_conclusion_loc2 =("xpath",'/html/body/div[2]/div/div')
    #质检意见下发
    Opinion_down_loc = ("id", 'b3')

    # 质检结论选择
    def iptconclusion(self,value):
        self.time(10)
        self.select_value(self.ipt_conclusion_loc,value)
        Log().info("质检结论:{}".format(value))
    #质检问题
    def inspectionpb(self):
        self.click_element(self.inspection_pbc_loc)
        self.click_element(self.inspection_pbc_loc2)
        self.click_element(self.inspection_pbc_loc3)
        self.click_element(self.inspection_pbc_loc4)
        Log().info("质检问题选择完成")
    #保存
    def savebutton(self):
        self.click_element(self.save_button_loc)
        Log().info("质检节点检查保存成功")

    #其他问题-质检结论
    def conclusion(self,value):
        self.select_value(self.conclusion_loc,value)
        Log().info("质检结论:{}".format(value))

    # 其他问题-质检问题
    def question(self,value):
        self.select_value(self.question_loc,value)
        Log().info("质检问题:{}".format(value))
    # 其他问题-操作保存
    def save_operation(self):
        self.click_element(self.save_operation_loc)
        self.click_element(self.elastic_loc)
        # alert = self.driver.switch_to.alert()
        # alert_text = alert.text
        # Log().info("弹框{}:".format(alert_text))
        # alert.dismiss()
        # Log().info("其他问题-操作保存成功")


    #待整改的质检节点-整体质检结论
    def overallconclusion(self):
        self.click_element(self.Overall_conclusion_loc)
        self.click_element(self.Overall_conclusion_loc2)
        Log().info("整体质检结论选择完成")
    #待整改的质检节点-质检意见下发
    def opinion_down(self):
        self.click_element(self.Opinion_down_loc)
        Log().info("质检意见下发点击成功")


    #质检审核总流程
    def quality_workflow(self):
        #点击质检审核-进入质检管理页面
        self.qualitymanagement()
        self.contno()
        #质检节点检查-质检结论-质检问题-保存
        self.switchwindows()      #切换窗口
        self.iptconclusion("通过")
        self.time(5)
        self.iptconclusion("整改")
        self.inspectionpb()
        self.savebutton()
        #其他问题-质检结论-质检问题-保存
        self.conclusion("不通过")
        self.question("其他")
        self.save_operation()
        # 待整改的质检节点-整体质检结论-质检意见下发
        self.overallconclusion()
        self.opinion_down()
