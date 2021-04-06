import time

from common.seleniunm_packaging import BasePage
from middleware.pages.accountopening import AccountOpening


class NewClientRegister(BasePage):
    """新增客户开户首页"""
    title = '管理平台-融航商品期权资管平台'

    # 定位到新增开户人姓名
    registrant_name = ('xpath', "//input[@id='rohon_cus_customename']")
    # 定位到证件号码
    id_number = ('xpath', "//input[@id='rohon_cus_idcard']")
    # 银行账号输入框
    bank_account_element = ('xpath', "//input[@id='rohon_cus_bankaccount']")
    # 输入联系电话
    phone_element = ('xpath', "//input[@id='rohon_cus_telphone']")
    # 定位电子邮件
    mail_element = ('xpath', "//input[@id='rohon_cus_email']")
    # 定位联系地址
    site_element = ('xpath', "//input[@id='rohon_cus_address']")
    # 定位到邮编
    postcode_element = ('xpath', "//input[@id='rohon_cus_zipcode']")
    # 获取到实际结果
    get_assert_element = ('xpath', "//div[@id='popup_message']")
    # 获取到实际结果:该账户已存在
    get_assert_element2 = ('xpath', "//div[@style='background-color:#fafafa;height:70px;text-align:left;padding-left:150px;padding-right:50px;vertical-align: middle;']")
    # 获取到窗口的确定
    win_queding = ('xpath', "//input[@id='popup_close']")
    # 获取到第二套确定按钮
    win_queding2 = ('xpath', "//input[@id='popup_ok']")
    # 定位到下一步按钮
    next_step = ('xpath', "//input[@id='next']")
    # 定位完成按钮
    wancheng = ('xpath', "//input[@id='queding']")

    def input_registrant_name(self, name):
        """输入开户人姓名"""
        self.find_element(self.registrant_name).send_keys(name)
        return self

    def input_number(self, number):
        """输入证件号码"""
        self.find_element(self.id_number).send_keys(number)
        return self

    def click_next(self):
        """点击下一步按钮"""
        self.click(self.next_step)
        time.sleep(1)
        return self

    def input_bank_account(self):
        """输入银行账号"""
        self.find_element(self.bank_account_element).send_keys('4548545687865132565')
        return self

    def input_phone(self):
        """输入联系电话"""
        self.find_element(self.phone_element).send_keys('16600281508')
        return self

    def input_mail(self):
        """输入邮件"""
        self.find_element(self.mail_element).send_keys('386160165@qq.com')
        return self

    def input_site(self):
        """输入联系地址"""
        self.find_element(self.site_element).send_keys('上海市浦东新')
        return self

    def input_postcode(self):
        """输入邮编"""
        self.find_element(self.postcode_element).send_keys('123456')
        return self

    def get_assert(self):
        """获取到实际结果"""
        el = self.find_element(self.get_assert_element).text
        return el

    def get_assert2(self):
        """获取到实际结果：输入的证件号号码不合法！和该用户已存在需要用这个"""
        time.sleep(1)
        el = self.find_element(self.get_assert_element2).text
        return el

    def clice_queding(self):
        """点击确定按钮"""
        self.click(self.win_queding)
        return self

    def empty_message_input(self):
        """清空输入框"""
        self.find_element(self.registrant_name).clear()
        self.find_element(self.id_number).clear()
        self.find_element(self.bank_account_element).clear()
        self.find_element(self.phone_element).clear()
        self.find_element(self.mail_element).clear()
        self.find_element(self.site_element).clear()
        self.find_element(self.postcode_element).clear()
        return self

    def clice_queding2(self):
        """点击确定按钮"""
        self.click(self.win_queding2)
        return self

    def click_next2(self):
        """点击下一步按钮"""
        self.click(self.next_step)
        time.sleep(1)
        return AccountOpening(self.driver)

    def select_product1(self, product1):
        """选择产品"""
        product_element = ('xpath', "//img[@id='{}']".format(product1))
        self.click(product_element)
        return self