"""核算信息页面"""
import re
import time
from math import ceil

from selenium.webdriver.support.select import Select

from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class TheMinimumOrder(BasePage):
    """账户历史页面"""
    title = '管理平台-融航商品期权资管平台'

    # 点击新建
    xinjian_element = ('xpath', "//span[text()='新建']")
    # 定位到品种id选择框
    variety_select_element = ('xpath', "//select[@id='opprodelimonthminmul_product']")
    # 定位到输入最小下单手数倍数
    opprodelimonthminmul_MinMulVolume_element = ('xpath', "//input[@id='opprodelimonthminmul_MinMulVolume']")
    # 定位到期货品种默认保证金率配置的确认按钮
    queding = ('xpath', "//input[@id='queding']")
    # 定位到窗口的确认按钮
    queren2 = ('xpath', "//input[@id='popup_ok']")
    # 定位获取结果元素
    actual_result = ('xpath', "//div//div[@id='popup_message']")
    # 获取总记录的条数
    pagebar_txt_element = ('xpath', "//span[@class='pagebar_txt']")
    # 获取品种代码
    element = ('xpath', "//td[@class='table_content_center']")
    # 下一页
    sheet_left_element = ('xpath', "//img[@alt='向右']")



    def variety_configuration_queding(self):
        """点击期货品种默认保证金率配置(和下一步通用)"""
        time.sleep(1)
        self.click(self.queding)
        return self

    def opprodelimonthminmul_MinMulVolume(self):
        """输入最小下单手数倍数"""
        self.find_element(self.opprodelimonthminmul_MinMulVolume_element).send_keys('10')
        return self

    def variety_select(self):
        """期货品种默认保证金率配置，选择品种"""
        js = "document.getElementById(\"opprodelimonthminmul_product\").style.display='block'"
        self.driver.execute_script(js)
        select_elem = self.find_element(self.variety_select_element)
        select = Select(select_elem)
        select.select_by_value('TCFFEX')
        time.sleep(1)
        return self

    def click_xinjian(self):
        """点击新建"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.xinjian_element)
        return self

    def get_chaxun_result(self):
        """获取结果"""
        time.sleep(1)
        Handmore = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")
        el = self.find_element(Handmore).text
        return el

    def select_account(self, account):
        """选择操作账户"""
        account_element = ('xpath', "//span[text()='{}']//preceding-sibling::label".format(account))
        self.click(account_element)

    def pagebar_txt(self):
        """获取当前的总条数"""
        el = self.find_element(self.pagebar_txt_element).text
        res = re.search(r"\d.", el)
        data = ceil(int(res.group())/10)
        return data

    def Look_for_the_element(self):
        """循环查找对比页面的元素"""
        i = 1
        while i <= self.pagebar_txt():
            data = self.find_elements(self.element)
            for e in data:
                if e.text == 'T':
                    return e.text
            self.click(self.sheet_left_element)
            i += 1

    def window_affirm2(self):
        """确认按钮用于第一个确认无法定位到的时候"""
        time.sleep(1)
        self.click(self.queren2)
        return self

    def get_actual(self):
        """获取实际结果"""
        el = self.find_element(self.actual_result).text
        return el

    def shanchu(self):
        """删除交割月合约交易最小手数倍数"""
        element = ('xpath', "//td[contains(text(),'T')]//following-sibling::td//following-sibling::td")
        self.click(element)
        return self
