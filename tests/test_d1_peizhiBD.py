import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestPeizhiBD(unittest.TestCase):
    """配置期货报单限制"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(
            cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_peizhiBD_a1_succeed(self):
        """期货品种单笔最大保证金/报单配置的测试用例"""
        accountopening2 = self.accountopening.peizhiBD()
        data = accountopening2.Varieties_limit().variety_select3().bjMaxCost().pricepercent().bjMaxVol()\
            .bjCloseMaxVol().OpenMinVol().CloseMinVol().variety_configuration_queding2().get_CloseMinVol()
        accountopening2.shanchu().window_affirm2()
        try:
            self.assertTrue(data['品种/合约代码'] == 'TF')
            self.assertTrue(data['最大保证金'] == '1,000,000.00')
            self.assertTrue(data['最大报单开仓数量'] == '10000')
            self.assertTrue(data['最大报单平仓数量'] == '10000')
            self.assertTrue(data['报价限制比例'] == '50.0')
            self.assertTrue(data['最小报单开仓数量'] == '1')
            self.assertTrue(data['最小报单平仓数量'] == '1')
            logging.info('配置期货报单限制的用例通过')
        except AssertionError as err:
            logging.error('配置期货报单限制的用例不通过')
            raise err

    def test_peizhiBD_a2_succeed(self):
        """期货合约单笔最大保证金/报单配置的测试用例"""
        self.driver.refresh()
        accountopening = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(self.data).peizhiBD()

        data = accountopening.Contract_limit().import_contract2().bjMaxCost().pricepercent().bjMaxVol()\
            .bjCloseMaxVol().OpenMinVol().CloseMinVol().variety_configuration_queding2().get_CloseMinVol2()
        accountopening.shanchu().window_affirm2()
        try:
            self.assertTrue(data['品种/合约代码'] == Hadnler.yaml['contract'])
            self.assertTrue(data['最大保证金'] == '1,000,000.00')
            self.assertTrue(data['最大报单开仓数量'] == '10000')
            self.assertTrue(data['最大报单平仓数量'] == '10000')
            self.assertTrue(data['报价限制比例'] == '50.0')
            self.assertTrue(data['最小报单开仓数量'] == '1')
            self.assertTrue(data['最小报单平仓数量'] == '1')
            logging.info('配置期货报单限制的用例通过')
        except AssertionError as err:
            logging.error('配置期货报单限制的用例不通过')
            raise err

    def test_peizhiBD_a3_succeed(self):
        """期货风控方案的用例"""
        self.driver.refresh()
        accountopening = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(self.data).fengkongFA()
        data = accountopening.variety_configuration_queding2().get_actual()

        try:
            self.assertTrue(data == '配置成功')
            logging.info('期货风控方案的用例通过')
        except AssertionError as err:
            logging.error('期货风控方案的用例不通过')
            raise err

    def test_peizhiBD_a4_succeed(self):
        """IP白名单绑定-单一ip的用例"""
        self.driver.refresh()
        accountopening = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(self.data).IPBMD()
        data = accountopening.Added_Whitelist().opipfilter_ipbegin().variety_configuration_queding2().window_affirm2()\
            .get_opipfilter_ipbegin()

        accountopening.shanchu().window_affirm2().window_affirm2()
        try:
            self.assertTrue(data['IP限制开始段'] == '192.168.1.100')
            self.assertTrue(data['IP限制结束段'] == '192.168.1.100')
            logging.info('IP白名单绑定-单一ip的用例通过')
        except AssertionError as err:
            logging.error('IP白名单绑定-单一ip的用例不通过')
            raise err

    def test_peizhiBD_a5_succeed(self):
        """IP白名单绑定-ip段的用例"""
        self.driver.refresh()
        accountopening = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(self.data).IPBMD()
        data = accountopening.Added_Whitelist_combination().opipfilter_ipbegin().opipfilter_ipend().\
            variety_configuration_queding2().window_affirm2().get_opipfilter_ipbegin()
        accountopening.shanchu().window_affirm2().window_affirm2()
        try:
            self.assertTrue(data['IP限制开始段'] == '192.168.1.100')
            self.assertTrue(data['IP限制结束段'] == '192.168.1.110')
            logging.info('IP白名单绑定-ip段的用例通过')
        except AssertionError as err:
            logging.error('IP白名单绑定-ip段的用例不通过')
            raise err

    def test_peizhiBD_a6_succeed(self):
        """MAC白名单绑定的用例"""
        self.driver.refresh()
        accountopening = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(self.data).MACBMD()
        data = accountopening.click_macipxinjian().opmacfilter_mac().variety_configuration_queding2().window_affirm2()\
            .get_opmacfilter_mac()
        accountopening.shanchu().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data == '2A-CD-C4-D7-8C-5D')
            logging.info('MAC白名单绑定的用例通过')
        except AssertionError as err:
            logging.error('MAC白名单绑定的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
