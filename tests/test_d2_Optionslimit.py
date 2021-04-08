import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestOptionslimit(unittest.TestCase):
    """期权开仓限制"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '13826813511'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_peizhiBD_a1_succeed(self):
        """期权开仓限制的测试用例"""
        accountopening = self.accountopening.OptionOpenLimit()
        data = accountopening.click_macipxinjian().product_CF().variety_configuration_queding2().window_affirm2().get_product()
        accountopening.delete_product_CF().positionschecks().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['权利仓'] == '可交易')
            self.assertTrue(data['义务仓'] == '可交易')
            self.assertTrue(data['标的品种/合约'] == 'CF')

            logging.info('期权开仓限制的用例通过')
        except AssertionError as err:
            logging.error('期权开仓限制的用例不通过')
            raise err

    def test_peizhiBD_a2_succeed(self):
        """期权持仓限制的测试用例"""
        self.driver.refresh()
        accountopening = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(
            self.data).OptPositionLimit()
        data = accountopening.click_macipxinjian().faceoppositionlimit().xuanze_pz().duotouall()\
            .kongtouall().variety_configuration_queding2().window_affirm2().get_OptPositionLimit()
        print(data)
        accountopening.click_quanxuan().shanchu().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['限制的账户名'] == self.data)
            self.assertTrue(data['限制的账户类型'] == '操作账户')
            self.assertTrue(data['标的品种或者标的合约'] == 'IO')
            logging.info('期权持仓限制的用例通过')
        except AssertionError as err:
            logging.error('期权持仓限制的用例不通过')
            raise err

    def test_peizhiBD_a3_succeed(self):
        """期权下单量限制的测试用例"""
        self.driver.refresh()
        accountopening = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(
            self.data).OrderVolumeLimit()
        data = accountopening.click_macipxinjian().btnselectopordervolumelimit_objcode().opordervolumelimit_maxmarketordervolume(). \
            opordervolumelimit_maxlimitordervolume().variety_configuration_queding2().window_affirm2().get_OptPositionLimit2()

        accountopening.click_quanxuan2().shanchu3().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['限制的账户名'] == self.data)
            self.assertTrue(data['限制的账户类型'] == '操作账户')
            self.assertTrue(data['标的品种或者标的合约'] == 'IO')
            self.assertTrue(data['限价单每次最大下单手数'] == '10000')
            self.assertTrue(data['市价单每次最大下单手数'] == '10000')
            logging.info('期权下单量限制的用例通过')
        except AssertionError as err:
            logging.error('期权下单量限制的用例不通过')
            raise err

    def test_peizhiBD_a4_succeed(self):
        """期权下单量限制的测试用例"""
        self.driver.refresh()
        accountopening = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(
            self.data).CancelVolumeLimit()
        data = accountopening.click_macipxinjian().btnselectopcanclevolumelimit_objcode()\
            .opcanclevolumelimit_maxcanclenumberlimitbyoneday().variety_configuration_queding2().window_affirm2().get_OptPositionLimit2()
        accountopening.click_quanxuan2().shanchu3().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['限制的账户名'] == self.data)
            self.assertTrue(data['限制的账户类型'] == '操作账户')
            self.assertTrue(data['标的品种或者标的合约'] == 'IO')
            self.assertTrue(data['市价单每次最大下单手数'] == '10000')
            logging.info('期权下单量限制的用例通过')
        except AssertionError as err:
            logging.error('期权下单量限制的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
