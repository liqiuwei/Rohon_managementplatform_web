import time
import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid

from middleware.pages.homepage import IndexPage

logging = Hadnler.logger

@ddt.ddt
class TestSettingFundst(unittest.TestCase):
    """期货合约默认保证金率配置"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = 'TTCZ'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).instrumentmargin()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_settingfundst_a1_succeed(self):
        """期货合约默认保证金率配置的用例"""
        data = self.accountopening.variety_earnest_newly().import_contract().number_earnest('100').amount_margin_rate('10')\
            .variety_configuration_queding().get_Hand_more()
        try:
            self.assertTrue(data['手数多金额是'] == '100.00 元')
            self.assertTrue(data['金额多金额是'] == '10.00%')
            self.assertTrue(self.accountopening.isPresent2(Hadnler.yaml['contract']))
            logging.info('期货合约默认保证金率配置的用例用例通过')
        except AssertionError as err:
            logging.error('期货合约默认保证金率配置的用例用例不通过')
            raise err
        self.accountopening.click_quanxuan().click_plscaccountmargincode2().window_affirm2()


if __name__ == '__main__':
    unittest.main()

