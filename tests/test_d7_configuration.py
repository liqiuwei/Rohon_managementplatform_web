import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestConfiguration(unittest.TestCase):
    """系统配置"""

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.data = Hadnler.name
        # cls.data = '李秋维'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_Configuration_a1_succeed(self):
        """客户管理的测试用例"""
        data = self.accountopening.click_system_configuration().click_opencustomerlist().input_account(self.data)\
            .click_chaxun().get_jieguo()

        try:
            self.assertTrue(data == self.data)
            logging.info('可交易品种/合约模板配置的用例通过')
        except AssertionError as err:
            logging.error('可交易品种/合约模板配置的用例不通过')
            raise err

    def test_Configuration_a3_succeed(self):
        """权限管理的测试用例"""
        self.driver.refresh()
        data = self.accountopening.click_system_configuration().click_powermanagerlist()
        data.variety_earnest_newly().click_rohon_gm_groupname().click_zijindiaoboyuan().variety_configuration_queding()

        try:
            self.assertTrue(data.isPresent2())
            data.click_delete().window_affirm2().window_affirm2()
            logging.info('权限管理的用例通过')
        except AssertionError as err:
            logging.error('权限管理的用例不通过')
            raise err

    def test_Configuration_a4_succeed(self):
        """银行管理的测试用例"""
        self.driver.refresh()
        banking_management = self.accountopening.click_system_configuration().click_banking_managemen()
        data = banking_management.variety_earnest_newly().rohon_bk_bankname().variety_configuration_queding().shanchu().result()
        try:
            self.assertTrue(data == '确定要删除自动化测试得银行卡数据吗？')
            banking_management.window_affirm2()
            logging.info('权限管理的用例通过')
        except AssertionError as err:
            logging.error('权限管理的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
