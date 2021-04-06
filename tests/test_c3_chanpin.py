import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestBindingProducts(unittest.TestCase):
    """绑定产品"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).chanpin()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_BindingProducts_a1_succeed(self):
        """绑定产品"""
        data = self.accountopening.get_chanpin_result()
        try:
            self.assertTrue(data == '操作账户[{}]绑定产品'.format(self.data))
            logging.info('绑定的用例通过')
        except AssertionError as err:
            logging.error('绑定产品的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
