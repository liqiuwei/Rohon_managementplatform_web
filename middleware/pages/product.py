"""新增产品页面"""
import time

from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class IncreaseProduct(BasePage):
    title = '管理平台-融航商品期权资管平台'
    URL = Hadnler.yaml['host'] + Hadnler.yaml['path']

    # 搜索输入框
    Search_input_box = ('xpath', "//input[@class='sousuo_button ac_input']")
    # 搜索按钮
    search = ('xpath', "//input[@class='sousuo_img']")
    # 定位产品名称输入框
    user_product = ('xpath', "//input[@id='groupname']")
    # 定位到产品别名输入框
    user_alias = ('xpath', "//input[@id='synonymname']")
    # 定位到确认按钮
    queding = ('xpath', "//input[@id='queding']")
    # 获取到失败的结果
    get_result_error = ('xpath', "//div[@style='background-color:#fafafa;height:70px;text-align:left;padding-left:150px;padding-right:50px;vertical-align: middle;']")
    # 定位到弹框的确认按钮
    windos_queding = ('xpath', "//input[@id='popup_ok']")
    # 定位添加成功产品的名称
    succeed_product = ('xpath', "//td[contains(text(),'李秋维哑场仫庐源萃公司')]")
    # 定位穿透式监管终端信息上报方式
    Order = ('xpath', "//p[@id='subInfoTypeP']")
    # 定位到交易员直接下单
    trader = ('xpath', "//li[text()='交易员直接下单']")

    def get(self):
        self.driver.get(self.URL)
        time.sleep(1)
        return self

    def get_balance(self):
        el = self.wait_element_visible(self.user_product)
        return el.text[:-1]

    def import_product_name(self, name):
        """输入产品名称"""
        self.find_element(self.user_product).send_keys(name)
        return self

    def import_product_alias(self, alias):
        """输入产品别名"""
        self.find_element(self.user_alias).send_keys(alias)
        return self

    def click_queren(self):
        """点击确认按钮"""
        self.click(self.queding)
        return self

    def get_error(self):
        """获取错误的提示文本"""
        el = self.wait_element_visible(self.get_result_error).text
        return el

    def click_window_queding(self):
        """点击弹框的确认按钮"""
        self.click(self.windos_queding)
        time.sleep(1)
        return self

    def empty_message_input(self):
        """清空输入框"""
        self.find_element(self.user_product).clear()
        self.find_element(self.user_alias).clear()
        return self

    def get_company_name(self, name):
        """获取到新增成功的产品"""
        el = self.find_element(('xpath', "//td[contains(text(),'{}')]".format(name)))
        return el.text

    def select_order_way(self):
        """选择交易员直接下单"""
        self.click(self.Order)
        time.sleep(1)
        self.click(self.trader)
        return self

    def input_product(self, account):
        """搜索框输入产品"""
        time.sleep(1)
        self.find_element(self.Search_input_box).send_keys(account)
        return self

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.search)
        time.sleep(1)
        return self