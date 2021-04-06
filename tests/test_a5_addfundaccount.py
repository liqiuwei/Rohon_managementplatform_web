import unittest
import ddt as ddt
import pytest

from middleware.heandler import Hadnler
from middleware.pages.addfundaccount import AddFundAccount
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger
data = Hadnler().excel('web_New_capital_account_cases.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')



@ddt.ddt
class TestNewlyCompany(unittest.TestCase):
    """新增资金账户"""

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.admin_page = IndexPage(cls.driver)
        cls.admin_page.click_capital_account_allocation().new_capital_account().select_qihuo()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    @ddt.data(*data_error)
    def test_capital_1_error(self, test_info):
        """新增资金账户失败的用例"""
        logging.info('开始测试新增资金账户失败的用例')
        addfundaccount = AddFundAccount(self.driver)
        if test_info['type'] == 1:
            actual = addfundaccount.import_name(eval(test_info['data'])['name']). \
                import_password(eval(test_info['data'])['password']). \
                select_company().select_product(Hadnler.establish_company).import_account(
                eval(test_info['data'])['account']).click_confirm().get_result22()
            addfundaccount.click_abnormal_confirm().empty_message_input()
        else:
            actual = addfundaccount.import_name(eval(test_info['data'])['name']). \
                import_password(eval(test_info['data'])['password']). \
                select_company().select_product(Hadnler.establish_company).import_account(
                eval(test_info['data'])['account']).click_confirm().get_result()
            addfundaccount.click_window_confirm().empty_message_input()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(actual == test_info['expected'])
            logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    @ddt.data(*data_success)
    def test_capital_2_succeed(self, test_info):
        """新增资金账户成功的用例"""
        logging.info('开始测试新增资金账户成功的用例')
        addfundaccount = AddFundAccount(self.driver)
        data = test_info['data']
        data = Hadnler().replace_data(data)
        expected = test_info['expected']
        expected = expected.replace('#mobile#', eval(data)['account'])
        actual = addfundaccount.get().click_capital_account_allocation().new_capital_account(). \
            select_qihuo().import_name(eval(test_info['data'])['name']).import_account(
            eval(data)['account']). \
            import_password(eval(test_info['data'])['password']). \
            select_company().select_product(Hadnler.establish_company).select_pneumatic(Hadnler.digits).click_confirm(). \
            input_capital(eval(data)['account']).click_search().get_company_name(eval(data)['account'])
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(expected, actual))
            self.assertTrue(actual == expected)
            logging.info('第{}条成功测试用例通过'.format(test_info['case_id']))
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
