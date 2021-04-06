import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestPinzhongTBJY(unittest.TestCase):
    """期货品种停板交易权限"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).pinzhongTBJY()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_pinzhongTBJY_a1_succeed(self):
        """期货品种停板交易权限的测试用例"""
        data = self.accountopening.click_configuration().warnHighLimit().highlimit().exchange_CFFEX().\
            variety_configuration_queding2().window_affirm2().get_pinzhongTBJY()
        self.accountopening.pinzhongTBJY_quanxuan().shanchu3().window_affirm2().window_affirm2()
        try:
            self.assertTrue(data['类型'] == '绝对值')
            self.assertTrue(data['一级风险'] == '10 Tick')
            self.assertTrue(data['一级风险触发时'] == '预警')
            self.assertTrue(data['二级风险'] == '9 Tick')
            self.assertTrue(data['二级风险触发时'] == '禁止开')
            logging.info('期货品种停板交易权限的用例通过')
        except AssertionError as err:
            logging.error('期货品种停板交易权限的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
