"""核算信息页面"""
import time
from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class AccountHistoryManager(BasePage):
    """账户历史页面"""
    title = '管理平台-融航商品期权资管平台'

    # 定位到账号输入框
    account_element = ('xpath', "//input[@id='account']")
    # 点击查询按钮
    chaxun_element = ('xpath', "//span[text()='查询']")
    # 定位到账户输入框
    accountname_element = ('xpath', "//input[@id='accountname']")

    def input_account(self, account):
        """输入账户名称"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.find_element(self.account_element).send_keys(account)
        return self

    def click_chaxun(self):
        """点击查询"""
        self.click(self.chaxun_element)
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

    def accountname(self, account):
        """输入账户名称"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.find_element(self.accountname_element).send_keys(account)
        self.click(('xpath', "//li[text()='{}']".format(account)))
        return self