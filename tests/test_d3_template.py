import unittest
import ddt as ddt
from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestTemplate(unittest.TestCase):
    """操作账户配置里的模板"""

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

    def test_template_a1_succeed(self):
        """行权纪录的测试用例"""
        data = self.accountopening.ExerciseStatement().get_bangdingSXF_result()

        try:
            self.assertTrue(data == '账户[{}]行权记录历史列表'.format(self.data))
            logging.info('行权记录的用例通过')
        except AssertionError as err:
            logging.error('行权记录的用例不通过')
            raise err

    def test_template_a2_succeed(self):
        """绑定期货品种持仓配置模板的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(
            self.data).bangdingPZCC().get_bangdingSXF_result()

        try:
            self.assertTrue(data == '账户[{}]绑定期货品种持仓配置模板'.format(self.data))
            logging.info('绑定期货品种持仓配置模板的用例通过')
        except AssertionError as err:
            logging.error('绑定期货品种持仓配置模板的用例不通过')
            raise err

    def test_template_a3_succeed(self):
        """绑定期货报单限制模板的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(
            self.data).bangdingBDXZ().get_bangdingSXF_result()

        try:
            self.assertTrue(data == '账户[{}]绑定期货报单限制模板'.format(self.data))
            logging.info('绑定期货报单限制模板的用例通过')
        except AssertionError as err:
            logging.error('绑定期货报单限制模板的用例不通过')
            raise err

    def test_template_a4_succeed(self):
        """绑定期货品种停板交易权限模板的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(
            self.data).BindingProductlimitTemplate().get_bangdingSXF_result()

        try:
            self.assertTrue(data == '账户[{}]绑定期货品种停板交易权限模板'.format(self.data))
            logging.info('绑定期货品种停板交易权限模板的用例通过')
        except AssertionError as err:
            logging.error('绑定期货品种停板交易权限模板的用例不通过')
            raise err

    def test_template_a5_succeed(self):
        """手续费优惠规则配置的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(
            self.data).Shouxufeiyouhui().get_bangdingSXF_result()

        try:
            self.assertTrue(data == '账户[{}]手续费优惠规则'.format(self.data))
            logging.info('手续费优惠规则配置的用例通过')
        except AssertionError as err:
            logging.error('手续费优惠规则配置的用例不通过')
            raise err

    def test_template_a6_succeed(self):
        """绑定手续费优惠规则模板的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).operating_account_management2().input_account(
            self.data).click_search().click_operation(self.data).click_configuration(
            self.data).Shouxufeiyouhui2().get_bangdingSXF_result()

        try:
            self.assertTrue(data == '账户[{}]绑定手续费优惠规则模板'.format(self.data))
            logging.info('绑定手续费优惠规则模板的用例通过')
        except AssertionError as err:
            logging.error('绑定手续费优惠规则模板的用例不通过')
            raise err

if __name__ == '__main__':
    unittest.main()
