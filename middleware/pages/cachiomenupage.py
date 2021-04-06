"""资金划拨页面"""
import time
from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class CacHiomenu(BasePage):
    """资金划拨页面"""
    title = '管理平台-融航商品期权资管平台'

    # 定位到账号输入框
    account_element = ('xpath', "//input[@id='account']")
    # 点击查询按钮
    chaxun_element = ('xpath', "//span[text()='查询']")
    # 定位到账户输入框
    accountname_element = ('xpath', "//input[@id='accountname']")
    # 定位到新增
    variety_deposit = ('xpath', "//span[text()='新增']")
    # 定位到转入转出输入框
    roll_inroll_out = ('xpath', "//input[@id='MONEY']")
    # 定位完成按钮
    wancheng = ('xpath', "//input[@id='queding']")
    # 定位到窗口的确认按钮
    queren2 = ('xpath', "//input[@id='popup_ok']")
    # 搜索输入框
    Search_input_box = ('xpath', "//input[@class='sousuo_button ac_input']")
    # 点击搜索按钮
    shousuo_element = ('xpath', "//input[@alt='搜索']")

    def click_shousuo(self):
        """点击搜索"""
        self.click(self.shousuo_element)
        return self

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

    def get_chaxun_result2(self):
        """获取结果"""
        time.sleep(1)
        Handmore = ('xpath', "//td[@id='Account1']")
        el = self.find_element(Handmore).text

        Handmore2 = ('xpath', "//td[@id='Account1']//following-sibling::td//following-sibling::td")
        el2 = self.find_element(Handmore2).text

        return {'操作账户': el, '总资金': el2}

    def select_account(self, account):
        """选择操作账户"""
        account_element = ('xpath', "//span[text()='{}']//preceding-sibling::label".format(account))
        self.click(account_element)

    def accountname(self, account):
        """输入账户名称"""
        self.find_element(self.accountname_element).send_keys(account)
        self.click(('xpath', "//li[contains(text(),'{}')]".format(account)))
        return self

    def variety_earnest_newly(self):
        """点击新增按钮"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.variety_deposit)
        time.sleep(1)
        return self

    def transfer_amount(self, money='9000000'):
        """转入/转出输入框(劣后资金)"""
        self.Situation_box(self.roll_inroll_out)
        self.find_element(self.roll_inroll_out).send_keys(money)
        return self

    def click_wancheng(self):
        """点击完成按钮"""
        self.click(self.wancheng)
        time.sleep(1)
        return self

    def window_affirm2(self):
        """确认按钮用于第一个确认无法定位到的时候"""
        self.click(self.queren2)
        return self

    def input_product(self, account):
        """搜索框输入产品"""
        time.sleep(1)
        self.find_element(self.Search_input_box).send_keys(account)
        return self