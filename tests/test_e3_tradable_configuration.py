import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage
logging = Hadnler.logger


@ddt.ddt
class TestTradableConfiguration(unittest.TestCase):
    """全局可交易品种/合约"""
    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.admin_page = IndexPage(cls.driver)
        cls.TradableConfig = cls.admin_page.click_Variety_contract_allocation()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_tradable_a1_success(self):
        """全局可交易品种/合约配置成功用例"""
        logging.info('开始测试全局风险度配置成功的用例')
        actual = self.TradableConfig.click_config().click_ag().click_bu2().click_bu_zhuli().click_bu_cizhuli().\
            click_bu_zhulisan().clicl_queding().get_actual()
        actual2 = self.TradableConfig.clicl_win_queren().click_check().click_del().clicl_win_queren().get_actual()
        try:
            self.assertTrue(actual == '配置成功！')
            self.assertTrue(actual2 == '删除成功')
            logging.info('测试全局可交易品种/合约配置用例通过')
        except AssertionError as err:
            logging.error('测试全局可交易品种/合约配置用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
