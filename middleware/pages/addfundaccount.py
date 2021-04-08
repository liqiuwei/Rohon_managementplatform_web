"""新增资金账户页面"""
import time
from selenium.webdriver.support.select import Select

from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class AddFundAccount(BasePage):
    """新增资金账户页面"""
    title = '管理平台-融航商品期权资管平台'
    URL = Hadnler.yaml['host'] + Hadnler.yaml['path']
    # 定位期货按钮
    qihuo = ('xpath', "//img[@id='qihuo']")
    # 定位开户人姓名输入框
    name = ('xpath', "//input[@id='investorname']")
    # 定位密码输入框
    password_element = ('xpath', "//input[@id='password']")
    # 定位账户输入框元素
    account_element = ('xpath', "//input[@id='investorid']")
    # 定位到选择开户经纪公司的的下拉框
    select_brokerage_element = ('xpath', "//select[@id='brokerid']")
    # 搜索输入框
    Search_input_box = ('xpath', "//input[@class='sousuo_button ac_input']")
    # 搜索按钮
    search = ('xpath', "//input[@class='sousuo_img']")
    # 定位获取到结果
    result = ('xpath', "//div[@id='popup_message']")
    # 定位确定按钮
    queding = ('xpath', "//input[@id='queding']")
    # 定位窗口的确认按钮
    window_queding = ('xpath', "//input[@id='popup_close']")

    s = ('xpath',
         "//div[@style='background-color:#fafafa;height:70px;text-align:left;padding-left:150px;padding-right:50px;vertical-align: middle;']")
    # 账户重复的窗口内的确认
    abnormal_confirm = ('xpath', "//input[@id='popup_ok']")

    def get(self):
        from middleware.pages.homepage import IndexPage
        self.driver.get(self.URL)
        time.sleep(1)
        return IndexPage(self.driver)

    def select_qihuo(self):
        """选择期货选项"""
        time.sleep(1)
        self.click(self.qihuo)
        return self

    def import_name(self, name):
        """输入开户人姓名"""
        self.find_element(self.name).send_keys(name)
        return self

    def import_password(self, password):
        """输入密码"""
        self.find_element(self.password_element).send_keys(password)
        return self

    def import_account(self, account):
        """输入账户"""
        self.find_element(self.account_element).send_keys(account)
        return self

    def select_company(self):
        """选择经纪公司"""
        js = "document.getElementById(\"brokerid\").style.display='block'"
        self.driver.execute_script(js)
        time.sleep(1)
        select_elem = self.find_element(self.select_brokerage_element)
        select = Select(select_elem)
        select.select_by_visible_text(Hadnler.yaml['Economics'])
        return self

    def select_product(self, product):
        """选择产品"""
        product_element = ('xpath', "//img[@id='{}']".format(product))
        self.click(product_element)
        return self

    def select_pneumatic(self, pneumatic):
        """选择风控账户"""
        # 定位到选择风控账户按钮
        pneumatic_element = ('xpath', "//img[@id='{}']".format(pneumatic))
        self.click(pneumatic_element)
        return self

    def click_confirm(self):
        """点击确定按钮"""
        self.click(self.queding)
        return self

    def get_result(self):
        """获取结果"""
        el = self.find_element(self.result).text
        return el

    def empty_message_input(self):
        """清空输入框"""
        self.find_element(self.name).clear()
        self.find_element(self.password_element).clear()
        self.find_element(self.account_element).clear()
        return self

    def click_window_confirm(self):
        # 点击窗口内的确认按钮
        self.click(self.window_queding)
        return self

    def get_result22(self):
        """获取结果"""
        el = self.find_element(self.s).text
        return el

    def click_abnormal_confirm(self):
        """点击账户重复的确定按钮"""
        self.click(self.abnormal_confirm)
        return self

    def get_company_name(self, name):
        """获取到新增成功的资金账户"""
        time.sleep(1)
        el = self.find_element(('xpath', "//td[@value='{}']".format(name)))
        return el.text

    def input_capital(self, account):
        """搜索框输入资金账户"""
        time.sleep(1)
        self.find_element(self.Search_input_box).send_keys(account)
        return self

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.search)
        time.sleep(1)
        return self
