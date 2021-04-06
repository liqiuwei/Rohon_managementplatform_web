import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestBindingProducts(unittest.TestCase):
    """期货品种开仓权限详细配置"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).pinzhongkaicang()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_BindingProducts_a1_succeed(self):
        """期货品种开仓权限详细配置的测试用例"""
        data = self.accountopening.variety_earnest_newly().import_contract().HighPrice().LowPrice()\
            .variety_configuration_queding().get_pinzhongkaicang()
        self.accountopening.pinzhongkaicang_quanxuan().pinzhongkaicang_shanchu().window_affirm2()
        try:
            self.assertTrue(data['方向'] == '开多')
            self.assertTrue(data['上限'] == '1.0E7')
            self.assertTrue(data['下限'] == '1.0')
            logging.info('期货品种开仓权限详细配置的用例通过')
        except AssertionError as err:
            logging.error('期货品种开仓权限详细配置的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
