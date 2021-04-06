import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestTemplate(unittest.TestCase):
    """模板配置"""

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_template_a1_succeed(self):
        """可交易品种/合约模板配置的测试用例"""
        template = self.accountopening.click_template1()
        data = template.click_ProductNotCantradeAndCantradeTemplat().variety_earnest_newly2()\
            .rohon_acinte_name().click_wancheng2().researchString().click_operation().click_kejiaoyi().click_configuration()\
            .click_ag().click_wancheng2().window_affirm2().get_actual3()
        template.click_quanxuan3().shanchu2().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['品种代码'] == 'ag')
            self.assertTrue(data['合约'] == 'all')
            logging.info('可交易品种/合约模板配置的用例通过')
        except AssertionError as err:
            logging.error('可交易品种/合约模板配置的用例不通过')
            raise err

    def test_template_a2_succeed(self):
        """不可交易品种/合约模板配置的测试用例"""
        self.driver.refresh()
        template = self.accountopening.click_template1()
        data = template.click_ProductNotCantradeAndCantradeTemplat() \
            .researchString2().click_operation().click_bukejiaoyi().click_configuration() \
            .click_ag().click_wancheng2().window_affirm2().get_actual3()
        template.click_quanxuan3().shanchu2().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['品种代码'] == 'ag')
            self.assertTrue(data['合约'] == 'all')
            logging.info('可交易品种/合约模板配置的用例通过')
        except AssertionError as err:
            logging.error('可交易品种/合约模板配置的用例不通过')
            raise err

    def test_template_a4_succeed(self):
        """期权开仓限制的测试用例"""
        self.driver.refresh()
        template = self.accountopening.click_template1()
        data = template.click_ProductNotCantradeAndCantradeTemplat() \
            .researchString2().click_operation().click_qiquankaichang().click_macipxinjian().product_CF()\
            .variety_configuration_queding2().get_actual()
        template.window_affirm4().click_quxiao().researchString3().click_quanxuan().positionschecks().window_affirm2()

        try:
            self.assertTrue(data == '操作成功')
            logging.info('期权开仓限制的用例通过')
        except AssertionError as err:
            logging.error('期权开仓限制的用例不通过')
            raise err

    def test_template_a5_succeed(self):
        """手续费模板列表的测试用例"""
        self.driver.refresh()
        CommisionTempManager = self.accountopening.click_template1()
        data = CommisionTempManager.click_CommisionTempManager().variety_earnest_newly2().rohon_acinte_name2().\
            variety_configuration_queding().researchString3().get_jieguo()
        CommisionTempManager.click_quanxuan().positionschecks().window_affirm2()

        try:
            self.assertTrue(data == '测试模板名称')
            logging.info('手续费模板列表的用例通过')
        except AssertionError as err:
            logging.error('手续费模板列表的用例不通过')
            raise err

    def test_template_a6_succeed(self):
        """手续费优惠规则模板的测试用例"""
        self.driver.refresh()
        CommisionTempManager = self.accountopening.click_template1()
        data = CommisionTempManager.click_commissionFavRuleTemplate().variety_earnest_newly2().rohon_acinte_name().\
            variety_configuration_queding2().window_affirm2().researchString3().get_jieguo()
        CommisionTempManager.click_quanxuan().positionschecks().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data == '测试模板名称')
            logging.info('手续费优惠规则模板的用例通过')
        except AssertionError as err:
            logging.error('手续费优惠规则模板的用例不通过')
            raise err

    def test_template_a7_succeed(self):
        """报单限制模板的测试用例"""
        self.driver.refresh()
        CommisionTempManager = self.accountopening.click_template1()
        data = CommisionTempManager.click_mainmenu_menuselected().variety_earnest_newly3().rohon_acinte_name4().\
            variety_configuration_queding2().window_affirm2().researchString4().get_jieguo()
        CommisionTempManager.click_quanxuan2().positionschecks().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data == '测试模板名称')
            logging.info('报单限制模板的用例通过')
        except AssertionError as err:
            logging.error('报单限制模板的用例不通过')
            raise err

    def test_template_a8_succeed(self):
        """报单限制模板的测试用例"""
        self.driver.refresh()
        CommisionTempManager = self.accountopening.click_template1()
        data = CommisionTempManager.click_Variety_position_allocation().variety_earnest_newly3().rohon_acinte_name3().\
            variety_configuration_queding2().window_affirm2().researchString4().get_jieguo()
        CommisionTempManager.click_quanxuan().positionschecks().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data == '测试模板名称')
            logging.info('报单限制模板的用例通过')
        except AssertionError as err:
            logging.error('报单限制模板的用例不通过')
            raise err

    def test_template_a9_succeed(self):
        """报单限制模板的测试用例"""
        self.driver.refresh()
        CommisionTempManager = self.accountopening.click_template1()
        data = CommisionTempManager.click_Variety_suspended_trading().variety_earnest_newly3().rohon_acinte_name5().\
            variety_configuration_queding2().window_affirm2().researchString4().get_jieguo()
        CommisionTempManager.click_quanxuan().positionschecks().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data == '测试模板名称')
            logging.info('报单限制模板的用例通过')
        except AssertionError as err:
            logging.error('报单限制模板的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
