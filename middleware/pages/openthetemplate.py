import time
from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class OpenWarehousePermissionTemplate(BasePage):
    """品种开仓权限模板首页"""
    title = '管理平台-融航商品期权资管平台'

    # 定位到品种开仓权限模板新增按钮
    newcapitalaccount = ('xpath', "//span[@class='bar_button2']")
    # 定位到模板名称输入框
    template_name = ('xpath', "//input[@id='name']")
    # 定位到确定按钮
    queding = ('xpath', "//input[@id='queding']")
    # 定位到窗口得确认按钮
    win_queding = ('xpath', "//input[@id='popup_ok']")
    # 获取到实际结果
    result_element = ('xpath', "//div[@id='popup_message']")
    # 定位到操作里面的配置按钮
    config = ('xpath', "//li//a[contains(text(),'配置')]")
    # 定位到品种保证金的新增元素
    variety_deposit = ('xpath', "//span[text()='新增']")
    # 定位到合约id输入框
    contract = ('xpath', "//input[@id='ProductID']")
    # 定位到上限输入框
    upper_limit_element = ('xpath', "//input[@id='HighPrice']")
    # 定位到下限输入框
    floor = ('xpath', "//input[@id='LowPrice']")

    def new_capital_account(self):
        """点击新增（资金账号）"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.newcapitalaccount)
        return self

    def input_template_name(self, name):
        """定位到模板名称输入框"""
        self.find_element(self.template_name).send_keys(name)
        return self

    def click_queding(self):
        """点击确定按钮"""
        self.click(self.queding)
        return self

    def click_win_queding(self):
        """点击窗口得确定按钮"""
        self.click(self.win_queding)
        return self

    def click_operation(self, name):
        """点击操作按钮"""
        time.sleep(1)
        operation = ('xpath', "//td[@id='{}']//following-sibling::*//following-sibling::*".format(name))
        self.click(operation)
        return self

    def get_actual(self):
        """获取实际的结果"""
        time.sleep(1)
        el = self.find_element(self.result_element).text
        return el

    def empty_input(self):
        # 清空新增经纪公司输入框
        self.find_element(self.template_name).clear()
        return self

    def click_config(self):
        """点击操作下面的配置按钮"""
        self.click(self.config)
        return self

    def variety_earnest_newly(self):
        """点击品种保证金的新增按钮(后面新增通用)"""
        self.click(self.variety_deposit)
        time.sleep(1)
        return self

    def import_contract(self):
        """输入合约id"""
        self.find_element(self.contract).send_keys(Hadnler.yaml['contract'])
        time.sleep(1)
        return self

    def upper_limit(self):
        """输入上限"""
        self.find_element(self.upper_limit_element).send_keys('800')
        return self

    def upper_floor(self):
        """输入下限"""
        self.find_element(self.floor).send_keys('500')
        return self
