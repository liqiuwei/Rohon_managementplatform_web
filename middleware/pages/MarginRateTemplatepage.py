import time

from selenium.webdriver.support.select import Select

from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class MarginRateTemplate(BasePage):
    """保证金率模版首页"""
    title = '管理平台-融航商品期权资管平台'

    # 定位到品种保证金的新增元素
    variety_deposit = ('xpath', "//span[text()='新增']")
    # 定位到模板名称输入框
    template_name = ('xpath', "//input[@id='name']")
    # 定位到确定按钮
    queding = ('xpath', "//input[@id='queding']")
    # 获取到实际结果
    result_element = ('xpath', "//div[@id='popup_message']")
    # 定位到窗口得确认按钮
    win_queding = ('xpath', "//input[@id='popup_ok']")
    # 定位到操作里面的配置按钮
    config = ('xpath', "//li//a[contains(text(),'配置')]")
    # 定位到新增品种费率
    increased_variety =('xpath', "//span[text()='新增品种费率']")
    # 定位到品种id选择框
    variety_select_element = ('xpath', "//select[@id='ProductID']")
    # 定位到合约id输入框
    variety__element = ('xpath', "//input[@id='ProductID']")
    # 定位到选按手数保证金费率输入框
    number_earnest_element = ('xpath', "//input[@id='LMarginRateByVol']")
    # 定位到按金额保证金率输入框
    money_margin_rate = ('xpath', "//input[@id='LMarginRateByMoney']")
    # 定位到新增合约费率
    contract_rate_element = ('xpath', "//span[text()='新增合约费率']")

    def amount_margin_rate(self):
        """按金额保证金率"""
        self.find_element(self.money_margin_rate).send_keys('30')
        return self

    def number_earnest(self):
        """输入按手数保证金费率"""
        self.find_element(self.number_earnest_element).send_keys('200')
        return self

    def variety_select(self):
        """期货品种默认保证金率配置，选择品种"""
        js = "document.getElementById(\"ProductID\").style.display='block'"
        self.driver.execute_script(js)
        select_elem = self.find_element(self.variety_select_element)
        select = Select(select_elem)
        select.select_by_value('TF33344553CFFEX')
        time.sleep(1)
        return self

    def variety_earnest_newly(self):
        """点击新增品种费率"""
        self.click(self.increased_variety)
        time.sleep(1)
        return self

    def click_contract_rate(self):
        """点击新增新增合约费率"""
        self.click(self.contract_rate_element)
        time.sleep(1)
        return self

    def click_config(self):
        """点击操作下面的配置按钮"""
        self.click(self.config)
        return self

    def click_operation(self, name):
        """点击操作按钮"""
        time.sleep(1)
        operation = ('xpath', "//td[contains(text(),'{}')]//following-sibling::td//following-sibling::td".format(name))
        self.click(operation)
        return self

    def click_win_queding(self):
        """点击窗口得确定按钮"""
        self.click(self.win_queding)
        return self

    def get_actual(self):
        """获取实际的结果"""
        time.sleep(1)
        el = self.find_element(self.result_element).text
        return el

    def click_queding(self):
        """点击确定按钮"""
        self.click(self.queding)
        return self

    def new_capital_account(self):
        """点击新增（保证金率模版）"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.variety_deposit)
        return self

    def input_template_name(self, name):
        """输入模板名称"""
        self.find_element(self.template_name).send_keys(name)
        return self

    def empty_input(self):
        """清空模板名称输入框"""
        self.find_element(self.template_name).clear()
        return self

    def click_collocate(self):
        """点击配置"""
        data = self.find_elements(self.config)
        data[-1].click()
        return self

    def empty_input2(self):
        """清空按手数保证金率/按金额保证金率输入框"""
        self.find_element(self.money_margin_rate).clear()
        self.find_element(self.number_earnest_element).clear()
        return self

    def isPresent(self, Xpath):
        """判断元素是否存在"""
        try:
            self.driver.find_element_by_xpath(Xpath)
        except Exception as err:
            return False
        return True

    def import_contract(self):
        """输入合约id"""
        self.find_element(self.variety__element).send_keys(Hadnler.yaml['contract'])
        time.sleep(1)
        return self


