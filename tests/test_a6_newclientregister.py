import unittest
import ddt as ddt
import pytest

from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage
from middleware.pages.newclientregister import NewClientRegister

logging = Hadnler.logger
data = Hadnler().excel('web_newcustomer_account_cases.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')


@ddt.ddt
class TestNewCustomerAccount(unittest.TestCase):
    """新增客户开户"""
    @classmethod
    def setUpClass(cls) -> None:
        setattr(Hadnler, 'phone', Hadnler().mobile)
        setattr(Hadnler, 'name', Hadnler().establish_name())
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.admin_page = IndexPage(cls.driver)
        cls.admin_page.click_new_account()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('关闭浏览器')

    @ddt.data(*data_error)
    def test_new_customer_a1_error(self, test_info):
        """新增账户开户失败的用例"""
        logging.info('开始测试新增账户开户失败用例')
        newclientregister = NewClientRegister(self.driver)
        if test_info['type'] == 1:
            actual = newclientregister.input_registrant_name(eval(test_info['data'])['name']).\
                input_number(eval(test_info['data'])['number']).input_bank_account().input_phone()\
                .input_mail().input_site().input_postcode().click_next().get_assert()
            newclientregister.clice_queding().empty_message_input()
        else:
            actual = newclientregister.input_registrant_name(eval(test_info['data'])['name']).input_number(
                eval(test_info['data'])['number']).input_bank_account().input_phone() \
                .input_mail().input_site().input_postcode().click_next().get_assert2()
            newclientregister.clice_queding2().empty_message_input()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(actual == test_info['expected'])
            logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    @ddt.data(*data_success)
    def test_new_customer_a2_success(self, test_info):
        """新增账户开户成功的用例"""
        logging.info('开始测试新增账户开户成功用例')
        data = test_info['data']
        data = Hadnler().replace_data(data)
        newclientregister = NewClientRegister(self.driver)
        actual = newclientregister.input_registrant_name(eval(data)['name']).\
            input_number(eval(test_info['data'])['number']).input_bank_account().input_phone()\
            .input_mail().input_site().input_postcode().click_next2().account_type(Hadnler.phone).click_wancheng().\
            operating_account_management().input_account(Hadnler.phone).click_search().get_account(Hadnler.phone)
        try:
            self.assertTrue(actual == Hadnler.phone)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
