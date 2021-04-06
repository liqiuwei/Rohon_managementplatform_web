import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestProductPositions(unittest.TestCase):
    """期货品种持仓配置"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '13896812311'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).Variety_opening_prohibited()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_instrumentcommission_a1_succeed(self):
        """期货品种持仓限制配置"""
        data = self.accountopening.variety_earnest_newly().exchange_INE().variety_configuration_queding2()\
            .window_affirm2().get_result()
        print(data)
        self.accountopening.shanchu().window_affirm2().window_affirm2()
        try:
            self.assertTrue(data == '禁买开')
            logging.info('期货品种持仓限制配置的用例通过')
        except AssertionError as err:
            logging.error('期货品种持仓限制配置的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
