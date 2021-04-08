"""新增经纪公司页面"""

import time
from selenium.webdriver.support.select import Select
from common.seleniunm_packaging import BasePage


class EconomicsIncreased(BasePage):
    title = '管理平台-融航商品期权资管平台'
    # 定位公司名称输入框
    company_name_input = ('xpath', "//input[@id ='rohon_bkaddr_brokenname']")
    # 定位公司代码输入框
    company_code = ('xpath', "//input[@id ='rohon_bkaddr_brokenid']")
    # 定位交易服务器地址输入框
    ransaction_server = ('xpath', "//input[@id ='tradeaddr']")
    # 定位行情服务器地址
    market_server = ('xpath', "//input[@id='quotationaddr']")
    # 定位校验码输入框
    result = ('xpath', "//input[@id='rohon_verificationcode']")
    # 定位确定标签
    confirm_element = ('xpath', "//input[@id='queding']")
    # 定位到报错元素
    report_error = ('xpath', "//div[@id='popup_message']")
    # 弹框的确认按钮
    wicket_confirm = ('xpath', "//input[@id='popup_ok']")
    # 定位柜台选择下拉框
    select = ('xpath', "//select[@class='selectoption']")

    def enter_company_name(self, company_name):
        # 输入公司名称
        self.find_element(self.company_name_input).send_keys(company_name)
        return self

    def enter_company_code(self, company_code):
        # 输入公司代码
        self.find_element(self.company_code).send_keys(company_code)
        return self

    def import_deal_site(self, enter_address):
        # 输入交易服务器地址
        self.find_element(self.ransaction_server).send_keys(enter_address)
        return self

    def import_market_site(self, enter_address):
        # 输入行情服务器地址
        self.find_element(self.market_server).send_keys(enter_address)
        return self

    def import_result(self, result_code):
        # 输入校验码
        self.find_element(self.result).send_keys(result_code)
        return self

    def click_confirm(self):
        # 点击确定
        self.find_element(self.confirm_element).click()
        return self

    def get_error(self):
        # 获取到错误文本
        el = self.wait_element_visible(self.report_error).text
        return el

    def click_wicket_confirm(self):
        # 点击弹框的确认按钮
        self.click(self.wicket_confirm)
        # self.find_element(self.wicket_confirm).click()
        return self

    def empty_input(self):
        # 清空新增经纪公司输入框
        self.find_element(self.company_name_input).clear()
        self.find_element(self.company_code).clear()
        self.find_element(self.ransaction_server).clear()
        self.find_element(self.market_server).clear()
        self.find_element(self.result).clear()
        return self

    def select_counte(self):
        # 选择不同柜台
        js = "document.getElementById(\"rohon_bkaddr_platformtype\").style.display='block'"
        self.driver.execute_script(js)
        time.sleep(1)
        select_elem = self.find_element(self.select)
        select = Select(select_elem)
        select.select_by_visible_text('融航柜台')
        return self

    def get_company_name(self, name):
        """获取到新增成功的公司名称文本"""
        el = self.find_element(('xpath', "//td[@value='{}']".format(name)))
        return el.text
