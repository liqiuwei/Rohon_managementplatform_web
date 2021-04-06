import time
from common.seleniunm_packaging import BasePage


class AddRiskControlAccountPage(BasePage):
    """添加风控账号页面"""
    title = '管理平台-融航商品期权资管平台'

    # 搜索输入框
    Search_input_box = ('xpath', "//input[@class='sousuo_button ac_input']")
    # 搜索按钮
    search = ('xpath', "//input[@class='sousuo_img']")
    # 定位到账户输入框
    account_element = ('xpath', "//input[@id='rohon_riskctrlid']")
    # 定位到密码输入框
    password_element = ('xpath', "//input[@id='rohon_password']")
    # 定位到账户类型（基金经理）
    account_type_fund = ('xpath', "//img[@id='erji']")
    # 定位到账户类型（产品经理）
    account_type_product = ('xpath', "//img[@id='yiji']")
    # 定位到确定按钮
    queding = ('xpath', "//input[@id='queding']")
    # 获取到失败得字段
    result = ('xpath', "//div[@id='popup_message']")
    # 定位到弹框得确认按钮
    win_queding = ('xpath', "//input[@id='popup_ok']")
    # 定位到管理账户配置
    account_executive = ('xpath', '''//a[@onclick="fengkong('745459864')"]''')
    # 定位资金账户
    capital_account = ('xpath', "//span[text()='资金账户']")
    # 定位操作账户
    operating_account = ('xpath', "//span[contains(text(),'操作账户')]")
    # 定位到选择一个已存在得产品
    select_product = ('xpath', "//img[@id='16600281508']")
    # 定位一个已经存在得操作账户
    the_operating_account = ('xpath', "//img[@id='123456']")

    def input_account(self, account):
        """输入账户"""
        self.find_element(self.account_element).send_keys(account)
        return self

    def input_password(self, pwd):
        """输入密码"""
        self.find_element(self.password_element).send_keys(pwd)
        return self

    def select_type(self):
        """选择类型"""
        self.click(self.account_type_fund)
        return self

    def click_queding(self):
        """点击确定按钮"""
        self.click(self.queding)
        time.sleep(1)
        return self

    def get_actual(self):
        """获取到错误信息"""
        el = self.find_element(self.result).text
        return el

    def click_win_queding(self):
        """弹框得确认按钮"""
        self.click(self.win_queding)
        return self

    def empty(self):
        """清空账户和密码得输入框"""
        self.find_element(self.account_element).clear()
        self.find_element(self.password_element).clear()
        return self

    def configuration(self, account):
        """点击操作"""
        data = ('xpath', "//td[@id='{}']//following-sibling::td//following-sibling::td//following-sibling::td"
                         "//following-sibling::td".format(account))
        self.click(data)
        time.sleep(1)
        return self

    def click_account_executive(self, account):
        """点击管理账号配置"""
        account_executive = ('xpath', '''//a[@onclick="fengkong('{}')"]'''.format(account))
        self.click(account_executive)
        return self

    def click_capital_account(self):
        """点击资金账户"""
        self.click(self.capital_account)
        return self

    def click_operating_account(self):
        """点击操作账户"""
        self.click(self.operating_account)
        return self

    def click_product(self,product):
        """先择一个产品"""
        # 定位到选择一个已存在得资金账户
        select_product = ('xpath', "//img[@id='{}']".format(product))
        self.click(select_product)
        return self

    def select_operating_account(self):
        """先择一个操作账户"""
        self.click(self.the_operating_account)
        return self

    def get_Successful_account(self, account):
        """获取成功得账户"""
        self.isPresent("//td[@id='{}']".format(account))
        return self

    def input_risk(self, account):
        """搜索框输入账户"""
        time.sleep(1)
        self.find_element(self.Search_input_box).send_keys(account)
        return self

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.search)
        time.sleep(1)
        return self

    def isPresent(self, Xpath):
        """判断元素是否存在"""
        try:
            self.driver.find_element_by_xpath(Xpath)
        except Exception as err:
            return False
        return True