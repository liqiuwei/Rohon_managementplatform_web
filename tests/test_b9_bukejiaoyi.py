import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestProductPositions(unittest.TestCase):
    """期货可交易品种/合约配置"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '13896812311'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).bukejiaoyi()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_instrumentcommission_a1_succeed(self):
        """期货可交易品种/合约配置"""
        data = self.accountopening.click_configuration().click_ag().variety_configuration_queding2().window_affirm2()\
            .get_kejiaoyi_result()
        print(data)
        self.accountopening.click_quanxuan3().shanchu2().window_affirm2().window_affirm2()
        try:
            self.assertTrue(data == 'all')
            logging.info('期货可交易品种/合约配置的用例通过')
        except AssertionError as err:
            logging.error('期货可交易品种/合约配置的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
