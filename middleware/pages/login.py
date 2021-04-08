"""登录页面"""
import time

from common.seleniunm_packaging import BasePage
from middleware.pages.homepage import IndexPage
from middleware.heandler import Hadnler


class LoginPage(BasePage):
    # title = '欢迎登录'
    URL = Hadnler.yaml['host']
    # URL = URL = Hadnler.yaml['host'] + Hadnler.yaml['path']
    # 定位登录按钮
    login_btn_locator = ('xpath', "//img[@id='bnt']")
    # 定位账号输入框
    username_locator = ('xpath', "//input[@name='user.rohon_us_username']")
    # 定位密码输入框
    password_locator = ('xpath', "//input[@name='user.rohon_us_password']")
    # 定位错误文本
    error_locator = ('xpath', "//div[@id='popup_message']")
    # 定位隐藏标签
    conceal_error_message = 'xpath', "//div[@class='layui-layer-content']"
    # 登录之后的确定按钮
    confirm_element = ('xpath', "//input[@class='btn1_mouseout']")
    # 定位输入验证码输入框
    valicode_element = ("xpath", "//input[@id='valicode']")
    # 定位到验证码
    verification_code_element = ('xpath', "//img[@id='code']")

    def __init__(self, driver):
        self.driver = driver

    def get(self):
        """访问页面"""
        self.driver.get(self.URL)
        return self

    def login_error(self, username, password):
        """登录行为"""
        self.enter_username(username)
        self.enter_password(password)
        result = self.Identification_verification_code(self.verification_code_element)
        self.find_element(self.valicode_element).send_keys(result)
        self.find_element(self.login_btn_locator).click()
        return self

    def login_success(self, username, password):
        """登录行为"""
        self.enter_username(username)
        self.enter_password(password)
        result = self.Identification_verification_code(self.verification_code_element)
        self.find_element(self.valicode_element).send_keys(result)
        self.find_element(self.login_btn_locator).click()
        self.find_element(self.confirm_element).click()
        return IndexPage(self.driver)

    def enter_username(self, username):
        self.find_element(self.username_locator).send_keys(username)
        return self

    def enter_password(self, password):
        self.find_element(self.password_locator).send_keys(password)
        return self

    def get_error_message(self):
        """获取登录不成功的错误信息"""
        return self.find_element(self.error_locator).text

    def get_conceal_err_message(self):
        """显性等待账号或密码错误"""
        return self.wait_element_visible(self.conceal_error_message).text

    def confirm(self):
        self.find_element(self.confirm_element).click()
        return
