"""银行管理页面"""
import time
from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class BankingManagemen(BasePage):
    """银行管理页面"""
    title = '管理平台-融航商品期权资管平台'


    # 定位到品种保证金的新增元素
    variety_deposit = ('xpath', "//span[text()='新增']")
    # 银行名称
    rohon_bk_bankname_element = ('xpath', "//input[@id='rohon_bk_bankname']")
    # 定位到期货品种默认保证金率配置的确认按钮
    queding = ('xpath', "//input[@id='queding']")
    # 获取出入金审核成功得结果
    get_results = ('xpath', "//div[@id='popup_message']")
    # 定位到窗口的确认按钮
    queren2 = ('xpath', "//input[@id='popup_ok']")

    def variety_configuration_queding(self):
        """点击确定"""
        time.sleep(1)
        self.click(self.queding)
        return self

    def rohon_bk_bankname(self):
        """输入银行名称"""
        self.find_element(self.rohon_bk_bankname_element).send_keys('自动化测试得银行卡')
        return self

    def variety_earnest_newly(self):
        """点击品种保证金的新增按钮(后面新增通用)"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.variety_deposit)
        time.sleep(1)
        return self

    def shanchu(self):
        """删除"""
        Handmore = (
        'xpath', "//td[contains(text(),'自动化测试得银行卡')]//following-sibling::td//following-sibling::td/child::a")
        self.click(Handmore)
        return self

    def result(self):
        """获取审核成功得结果"""
        time.sleep(1)
        el = self.find_element(self.get_results).text
        return el

    def window_affirm2(self):
        """确认按钮用于第一个确认无法定位到的时候"""
        self.click(self.queren2)
        return self