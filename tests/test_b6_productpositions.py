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
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).productpositions()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_instrumentcommission_a1_succeed(self):
        """期货品种持仓限制配置"""
        data = self.accountopening.Limited_varieties().variety_select2().position_ceiling().Position_margin_limit()\
            .variety_configuration_queding().get_productpositions_result()
        self.accountopening.click_quanxuan2().positionschecks().window_affirm2().window_affirm2()
        try:
            self.assertTrue(data['持仓量上限'] == '100,000')
            self.assertTrue(data['持仓保证金上限'] == '2,000,000')
            self.assertTrue(data['品种名称'] == 'T')
            self.assertTrue(data['持仓类型'] == '投机')
            logging.info('期货品种持仓限制配置的用例通过')
        except AssertionError as err:
            logging.error('期货品种持仓限制配置的用例不通过')
            raise err

    def test_instrumentcommission_a2_succeed(self):
        """期货合约手续费率配置-绝对收取得用例"""
        data = self.accountopening.astrict().import_contract().position_ceiling().Position_margin_limit()\
            .variety_configuration_queding().get_productpositions_result2()
        self.accountopening.click_quanxuan2().positionschecks().window_affirm2().window_affirm2()
        try:
            self.assertTrue(data['持仓量上限'] == '100,000')
            self.assertTrue(data['持仓保证金上限'] == '2,000,000')
            self.assertTrue(data['品种名称'] == Hadnler.yaml['contract'])
            self.assertTrue(data['持仓类型'] == '投机')
            logging.info('期货品种持仓限制配置的用例通过')
        except AssertionError as err:
            logging.error('期货品种持仓限制配置的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
