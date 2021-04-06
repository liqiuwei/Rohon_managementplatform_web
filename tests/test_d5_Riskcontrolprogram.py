import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestReportQuery(unittest.TestCase):
    """产品-配置"""

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.data = Hadnler.establish_company
        cls.account = Hadnler.one__key_phone
        # cls.account = '16600281508'
        # cls.data = '自动化测试产品'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_Productioneditor_a1_succeed(self):
        """编辑产品的测试用例"""
        data = self.accountopening.click_capital_account_allocation().click_product_admin2().input_product(self.data).click_search().click_peizhi(self.data)\
            .DailyCheckReport().synonymname().oldrealaccountNum().accountNum().click_wancheng().get_actual()
        self.accountopening.click_audit_queren()

        try:
            self.assertTrue(data == '修改成功')
            logging.info('编辑产品的用例通过')
        except AssertionError as err:
            logging.error('编辑产品的用例不通过')
            raise err

    def test_Productioneditor_a2_succeed(self):
        """风控方案配置的测试用例"""
        self.driver.refresh()
        data = self.accountopening.click_capital_account_allocation().click_product_admin2().input_product(self.data).click_search().click_peizhi(self.data)\
            .fkfacp1().newly().RiskPlanName().click_wancheng().click_quanxuan().positionschecks().window_affirm2()\
            .get_actual()

        try:
            self.assertTrue(data == '删除成功')
            logging.info('风控方案配置的用例通过')
        except AssertionError as err:
            logging.error('风控方案配置的用例不通过')
            raise err

    def test_Productioneditor_a3_succeed(self):
        """风控区间配置的测试用例"""
        self.driver.refresh()
        data = self.accountopening.click_capital_account_allocation().click_product_admin2().input_product(self.data).click_search().click_peizhi(self.data)\
            .fkqjcp1().zengjiaqujian().click_select().select_yujingxian().input_net_worth().click_wancheng().get_actual()

        try:
            self.assertTrue(data == '配置成功')
            logging.info('风控区间配置的用例通过')
        except AssertionError as err:
            logging.error('风控区间配置的用例不通过')
            raise err

    def test_Productioneditor_a4_succeed(self):
        """产品早盘可交易品种/合约的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_zaopan1().click_Commission_configuration().click_ag()\
            .click_wancheng().window_affirm2().get_actual_result()
        accountopening.click_quanxuan2().shanchu3().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['品种代码'] == 'ag')
            self.assertTrue(data['合约'] == 'all')
            logging.info('产品早盘可交易品种/合约的用例通过')
        except AssertionError as err:
            logging.error('产品早盘可交易品种/合约的用例不通过')
            raise err

    def test_Productioneditor_a5_succeed(self):
        """产品夜盘可交易品种/合约的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_yepan1().click_Commission_configuration().click_ag()\
            .click_wancheng().window_affirm2().get_actual_result()
        accountopening.click_quanxuan2().shanchu3().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['品种代码'] == 'ag')
            self.assertTrue(data['合约'] == 'all')
            logging.info('产品夜盘可交易品种/合约的用例通过')
        except AssertionError as err:
            logging.error('产品夜盘可交易品种/合约的用例不通过')
            raise err

    def test_Productioneditor_a6_succeed(self):
        """当月交割品种的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_DYJG2().click_Commission_configuration().exchange_CFFEX()\
            .click_wancheng().window_affirm2().get_actual_result()
        accountopening.click_quanxuan2().shanchu3().window_affirm2().window_affirm2()

        try:
            self.assertTrue(data['品种代码'] == 'CFFEX')
            self.assertTrue(data['合约'] == 'all')
            logging.info('当月交割品种的用例通过')
        except AssertionError as err:
            logging.error('当月交割品种的用例不通过')
            raise err

    def test_Productioneditor_a7_succeed(self):
        """当平今转开仓的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_CTO1().get_actual2(self.data)
        try:
            self.assertTrue(data == '产品[{}]平今转开仓合约配置'.format(self.data))
            logging.info('平今转开仓的用例通过')
        except AssertionError as err:
            logging.error('平今转开仓的用例不通过')
            raise err

    def test_Productioneditor_a8_succeed(self):
        """板块管理的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_bankuaicp().get_actual3()
        try:
            self.assertTrue(data == '产品[{}]板块列表'.format(self.data))
            logging.info('板块管理的用例通过')
        except AssertionError as err:
            logging.error('板块管理的用例不通过')
            raise err

    def test_Productioneditor_a9_succeed(self):
        """费用管理的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_feiyong().get_actual4()

        try:
            self.assertTrue(data == '费用查询')
            logging.info('费用查询的用例通过')
        except AssertionError as err:
            logging.error('费用查询的用例不通过')
            raise err

    def test_Productioneditor_b1_succeed(self):
        """外部报单配置的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_waibubaodancp2()\
            .newly().select_account(self.account).exchange_CFFEX().click_wancheng().window_affirm2().get_actual5()

        accountopening.pinzhongTBJY_quanxuan().positionschecks().window_affirm2().window_affirm2()
        try:
            self.assertTrue(data['操作账户'] == self.account)
            self.assertTrue('T,IH,IO,TF,IF,IC,TS' in data['品种'])
            logging.info('外部报单配置的用例通过')
        except AssertionError as err:
            logging.error('外部报单配置的用例不通过')
            raise err

    def test_Productioneditor_b2_succeed(self):
        """品种交易模式的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_DailyCheckReport()\
            .newly().variety_select().click_wancheng().get_actual6()

        accountopening.click_quanxuan3().positionschecks().window_affirm2()
        try:
            self.assertTrue(data['品种'] == 'IF')
            self.assertTrue(data['交易模式'] == '按产品资金账户优先级' )
            logging.info('品种交易模式的用例通过')
        except AssertionError as err:
            logging.error('品种交易模式的用例不通过')
            raise err

    def test_Productioneditor_b3_succeed(self):
        """产品总结报告的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_DailyCheckReport2()\
            .get_actual7()

        try:
            self.assertTrue(data== '{} 产品总结报告'.format(self.data))
            logging.info('产品总结报告的用例通过')
        except AssertionError as err:
            logging.error('产品总结报告的用例不通过')
            raise err

    def test_Productioneditor_b4_succeed(self):
        """估值文件上传的测试用例"""
        self.driver.refresh()
        accountopening = self.accountopening.click_capital_account_allocation().click_product_admin2()
        data = accountopening.input_product(self.data).click_search().click_peizhi(self.data).click_guzhishangchuan()\
            .tradingday().click_myFile().click_wancheng().get_actual()

        try:
            self.assertTrue(data== '文件上传成功')
            logging.info('估值文件上传的用例通过')
        except AssertionError as err:
            logging.error('估值文件上传的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()