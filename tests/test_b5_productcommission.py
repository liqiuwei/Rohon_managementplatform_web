import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestSettingFundst(unittest.TestCase):
    """品种手续费率配置"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).productcommission()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_instrumentcommission_a1_succeed(self):
        """品种手续费率配置-绝对收取得用例"""
        data = self.accountopening.variety_earnest_newly().variety_select().shoushu_shouxufei().jine_shouxufei().\
            variety_configuration_queding().get_Hand_mor2()
        self.accountopening.click_quanxuan().plscaccountcommissionproduct().window_affirm2()
        try:
            self.assertTrue(data['按手数开仓'] == '100.00 元')
            self.assertTrue(data['按金额开仓'] == '10.00%')
            self.assertTrue(data['品种名称'] == 'T')
            self.assertTrue(data['收取方式'] == '绝对收取')
            logging.info('品种手续费率配置-绝对收取得用例通过')
        except AssertionError as err:
            logging.error('品种手续费率配置-绝对收取得用例不通过')
            raise err

    def test_instrumentcommission_a2_succeed(self):
        """品种手续费率配置-绝对收取得用例"""
        data = self.accountopening.variety_earnest_newly().ChargeType().variety_select().shoushu_shouxufei().jine_shouxufei(). \
            variety_configuration_queding().get_Hand_mor2()
        self.accountopening.click_quanxuan().plscaccountcommissionproduct().window_affirm2()
        try:
            self.assertTrue(data['按手数开仓'] == '100.00 元')
            self.assertTrue(data['按金额开仓'] == '10.00%')
            self.assertTrue(data['品种名称'] == 'T')
            self.assertTrue(data['收取方式'] == '相对资金账户绝对值收取')
            logging.info('期货合约手续费率配置-绝对收取得用例通过')
        except AssertionError as err:
            logging.error('期货合约手续费率配置-绝对收取得用例不通过')
            raise err

    def test_instrumentcommission_a3_succeed(self):
        """品种手续费率配置-绝对收取得用例"""
        data = self.accountopening.variety_earnest_newly().ChargeType3().variety_select().shoushu_shouxufei().jine_shouxufei(). \
            variety_configuration_queding().get_Hand_mor2()
        self.accountopening.click_quanxuan().plscaccountcommissionproduct().window_affirm2()
        try:
            self.assertTrue(data['按手数开仓'] == '100.00%')
            self.assertTrue(data['按金额开仓'] == '10.00%')
            self.assertTrue(data['品种名称'] == 'T')
            self.assertTrue(data['收取方式'] == '相对资金账户百分比加收')
            logging.info('期货合约手续费率配置-绝对收取得用例通过')
        except AssertionError as err:
            logging.error('期货合约手续费率配置-绝对收取得用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
