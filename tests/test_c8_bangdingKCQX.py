import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestBangdingKCQX(unittest.TestCase):
    """绑定期货品种开仓权限模板"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).bangdingKCQX()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_bangdingKCQX_a1_succeed(self):
        """绑定期货品种开仓权限模板的测试用例"""
        data = self.accountopening.get_bangdingSXF_result()
        self.accountopening.variety_configuration_queding2()
        try:
            self.assertTrue(data == '账户[{}]绑定期货品种开仓权限模板'.format(self.data))
            logging.info('绑定期货品种开仓权限模板的用例通过')
        except AssertionError as err:
            logging.error('绑定期货品种开仓权限模板的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
