import unittest
import ddt as ddt
import pytest

from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler
from middleware.pages.addriskcontrolaccount import AddRiskControlAccountPage
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger
data = Hadnler().excel('web_Increaseriskcontrolaccountt_cases.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')



@ddt.ddt
class TestAddRiskControlAccount(unittest.TestCase):
    """添加风控账户"""

    @classmethod
    def setUpClass(cls) -> None:
        setattr(Hadnler, 'digits', Hadnler().Nine_digits)
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.admin_page = IndexPage(cls.driver)
        cls.admin_page.click_risk_control_allocation().click_new_risk()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    @ddt.data(*data_error)
    def test_control_account_a1_error(self, test_info):
        """添加风控账户失败得用例"""
        logging.info('开始测试添加风控账户失败得用例')
        addriskcontrolaccount = AddRiskControlAccountPage(self.driver)
        actual = addriskcontrolaccount.input_account(eval(test_info['data'])['account']). \
            input_password(eval(test_info['data'])['pwd']).select_type(). \
            click_queding().get_actual()
        addriskcontrolaccount.click_win_queding().empty()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(test_info['expected'] == actual)
            logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    @ddt.data(*data_success)
    def test_control_account_a2_success(self, test_info):
        """添加风控账户成功的用例"""
        logging.info('开始测试添加风控账户成功的用例')
        data = test_info['data']
        data = Hadnler().replace_data(data)
        addriskcontrolaccount = AddRiskControlAccountPage(self.driver)
        addriskcontrolaccount.input_account(eval(data)['account']). \
            input_password(eval(test_info['data'])['pwd']).select_type(). \
            click_queding().input_risk(Hadnler.digits).click_search()
        try:
            self.assertTrue(addriskcontrolaccount.isPresent("//td[@id='{}']".format(Hadnler.digits)))
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err
    #
    # def test_control_account_a3_success(self):
    #     """风控账户添加资金账号用例"""
    #     logging.info('开始测试风控账户添加资金账号的用例')
    #     addriskcontrolaccount = AddRiskControlAccountPage(self.driver)
    #     actual = addriskcontrolaccount.configuration(Hadnler.digits).click_account_executive(
    #         Hadnler.digits).click_capital_account() \
    #         .click_product(Hadnler.establish_company).click_queding().get_actual()
    #     addriskcontrolaccount.click_win_queding()
    #     try:
    #         logging.info('预期结果:{}，实际结果:{}'.format('操作成功，重新启动风控后生效', actual))
    #         self.assertTrue(actual == '操作成功，重新启动风控后生效')
    #         logging.info('测试用例通过')
    #     except AssertionError as err:
    #         logging.error('测试用例不通过')
    #         raise err
    #
    # def test_control_account_a4_success(self):
    #     """风控账户添加操作账户用例"""
    #     logging.info('开始测试风控账户添加操作账户的用例')
    #     addriskcontrolaccount = AddRiskControlAccountPage(self.driver)
    #     actual = addriskcontrolaccount.click_operating_account() \
    #         .select_operating_account().click_queding().get_actual()
    #     addriskcontrolaccount.click_win_queding()
    #     try:
    #         logging.info('预期结果:{}，实际结果:{}'.format('操作成功，重新启动风控后生效', actual))
    #         self.assertTrue(actual == '操作成功，重新启动风控后生效')
    #         logging.info('测试用例通过')
    #     except AssertionError as err:
    #         logging.error('测试用例不通过')
    #         raise err


if __name__ == '__main__':
    unittest.main()
