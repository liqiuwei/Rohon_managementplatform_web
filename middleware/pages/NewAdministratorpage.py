import time

from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class NewAdministrator(BasePage):
    """新增管理员页面"""
    title = '管理平台-融航商品期权资管平台'
    URL = Hadnler.yaml['host'] + Hadnler.yaml['path']

    # 定位到登录名输入框
    name_element = ('xpath', "//input[@id='rohon_us_username']")
    # 定位到密码输入框
    pwd_element = ('xpath', "//input[@id='rohon_us_password']")
    # 定位到选择资金调拨员按钮
    allot_element = ('xpath', "//img[@myvalue='100']")
    # 定位到仅可查看自己开设的账户
    Check_the_account = ('xpath', "//img[@class='circle4']")
    # 定位搜索账号框
    search_element = ('xpath', "//input[@id='accountname']")
    # 定位确定按钮
    queding = ('xpath', "//input[@id='queding']")
    # 定位窗口得确定按钮
    win_queding = ('xpath', "//input[@id='popup_ok']")
    # 获取创建得账户
    get_account = ('xpath', "")
    # 搜索输入框
    Search_input_box = ('xpath', "//input[@class='sousuo_button ac_input']")
    # 搜索按钮
    search = ('xpath', "//input[@class='sousuo_img']")

    def input_name(self, name):
        """输入账号"""
        self.find_element(self.name_element).send_keys(name)
        return self

    def input_pwd(self, pwd):
        """输入密码"""
        self.find_element(self.pwd_element).send_keys(pwd)
        return self

    def click_allot(self):
        """点击资金调拨员"""
        self.click(self.allot_element)
        return self

    def click_Check_the_account(self):
        """点击取消仅可查看自己开设的账户"""
        self.click(self.Check_the_account)
        return self

    def select_operating_account(self, account):
        """选择操作账户"""
        account_element = ('xpath', "//li[text()='{}']".format(account))
        self.find_element(self.search_element).send_keys(account)
        time.sleep(1)
        self.click(account_element)
        return self

    def click_queding(self):
        """点击确定按钮"""
        self.click(self.queding)
        return self

    def click_winqueding(self):
        """点击窗口得确定按钮"""
        time.sleep(1)
        self.click(self.win_queding)
        return self

    def get_results(self, login):
        """获取到新增加得登录账户"""
        time.sleep(1)
        get_account = ('xpath', "//td[@value='{}']".format(login))
        el = self.find_element(get_account).text
        return el

    def input_account(self, account):
        """搜索框输入账户"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.find_element(self.Search_input_box).send_keys(account)
        return self

    def click_search(self):
        "点击搜索按钮"
        self.click(self.search)
        return self