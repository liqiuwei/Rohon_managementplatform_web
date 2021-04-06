import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestOtherConfiguration(unittest.TestCase):
    """其它配置"""

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_OtherConfiguration_a1_succeed(self):
        """终端认证配置的测试用例"""
        OtherConfiguration = self.accountopening.click_qitapeizi().click_AuthInfoDispose()
        data = OtherConfiguration.variety_earnest_newly().input_appid().variety_configuration_queding().\
            variety_configuration_queding2().window_affirm().search_appid().click_seek().shanchu().window_affirm2().result()
        try:
            self.assertTrue(data == '删除成功')
            logging.info('终端认证配置的用例通过')
        except AssertionError as err:
            logging.error('终端认证配置的用例不通过')
            raise err

    def test_OtherConfiguration_a2_succeed(self):
        """交割月最小下单手数的测试用例"""
        self.driver.refresh()
        prodelimonthminmul = self.accountopening.click_qitapeizi().click_prodelimonthminmul()
        data = prodelimonthminmul.click_xinjian().variety_select().opprodelimonthminmul_MinMulVolume().variety_configuration_queding()\
            .window_affirm2().Look_for_the_element()
        try:
            self.assertTrue(data == 'T')
            prodelimonthminmul.shanchu().window_affirm2()
            logging.info('交割月最小下单手数的用例通过')
        except AssertionError as err:
            logging.error('交割月最小下单手数的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
