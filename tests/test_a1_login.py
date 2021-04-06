import unittest
import ddt as ddt
import pytest

from middleware.heandler import Hadnler
from middleware.pages.login import LoginPage

logging = Hadnler.logger
data = Hadnler().excel('web_login_cases.xlsx')
data_error = data.read_data('login_error')
data_success = data.read_data('login_success')
logging.info('读取excel')



@ddt.ddt
class TestLogin(unittest.TestCase):
    """登录测试用例"""

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.driver = Hadnler().Launch_browser()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    @ddt.data(*data_error)
    def test_login_1_error(self, test_info):
        """登录失败"""
        logging.info('开始测试登录失败用例')
        login_page = LoginPage(self.driver)
        actual = login_page.get().login_error(username=eval(test_info['data'])['username'],
                                              password=eval(test_info['data'])['password']).get_error_message()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(actual == test_info['expected'])

            logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    @ddt.data(*data_success)
    def test_login_2_succee(self, test_info):
        """登录成功"""
        logging.info('开始测试登录成功用例')
        login_page = LoginPage(self.driver)
        actual = login_page.get().login_success(username=eval(test_info['data'])['username'],
                                                password=eval(test_info['data'])['password']).get_account_name()

        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(actual == test_info['expected'])
            logging.info('测试用例通过')
            logging.info('登录成功')

        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
