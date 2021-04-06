import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid

from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestSettingFundst(unittest.TestCase):
    """期货品种保证金率配置"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).pinzhongmargin()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_pinzhongmargin_a1_succeed(self):
        """期货品种保证金率配置-绝对收取的用例"""
        data = self.accountopening.variety_earnest_newly().variety_select().number_earnest().amount_margin_rate() \
            .variety_configuration_queding().get_Hand_mor2e()
        self.accountopening.click_quanxuan().click_plscaccountmargincode().window_affirm2()
        try:
            self.assertTrue(data['手数多金额是'] == '100.00 元')
            self.assertTrue(data['金额多金额是'] == '10.00%')
            self.assertTrue(data['品种名称'] == 'T')
            self.assertTrue(data['收取方式'] == '绝对收取')
            logging.info('期货品种保证金率配置-绝对收取的用例通过')
        except AssertionError as err:
            logging.error('期货品种保证金率配置-绝对收取的用例不通过')
            raise err

    def test_pinzhongmargin_a2_succeed(self):
        """期货品种保证金率配置-相对资金账户绝对值收取的用例"""
        data = self.accountopening.variety_earnest_newly().ChargeType().variety_select().number_earnest().amount_margin_rate() \
            .variety_configuration_queding().get_Hand_mor2e()
        self.accountopening.click_quanxuan().click_plscaccountmargincode().window_affirm2()
        try:
            self.assertTrue(data['手数多金额是'] == '100.00 元')
            self.assertTrue(data['金额多金额是'] == '10.00%')
            self.assertTrue(data['品种名称'] == 'T')
            self.assertTrue(data['收取方式'] == '相对资金账户绝对值收取')
            logging.info('期货品种保证金率配置-相对资金账户绝对值收取的用例通过')
        except AssertionError as err:
            logging.error('期货品种保证金率配置-相对资金账户绝对值收取的用例不通过')
            raise err

    def test_pinzhongmargin_a3_succeed(self):
        """期货品种保证金率配置-相对资金账户百分比加收的用例"""
        data = self.accountopening.variety_earnest_newly().ChargeType3().variety_select().number_earnest().amount_margin_rate() \
            .variety_configuration_queding().get_Hand_mor2e()
        self.accountopening.click_quanxuan().click_plscaccountmargincode().window_affirm2()
        try:
            self.assertTrue(data['手数多金额是'] == '100.00%')
            self.assertTrue(data['金额多金额是'] == '10.00%')
            self.assertTrue(data['品种名称'] == 'T')
            self.assertTrue(data['收取方式'] == '相对资金账户百分比加收')
            logging.info('期货品种保证金率配置-相对资金账户百分比加收的用例通过')
        except AssertionError as err:
            logging.error('期货品种保证金率配置-相对资金账户百分比加收的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
