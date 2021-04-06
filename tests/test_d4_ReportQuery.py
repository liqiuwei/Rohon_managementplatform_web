import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger


@ddt.ddt
class TestReportQuery(unittest.TestCase):
    """报单查询"""

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).click_ReportQuery()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_ReportQuery_a1_succeed(self):
        """报单查询资金的测试用例"""
        data = self.accountopening.accountname(self.data).click_zijin().get_bangdingSXF_result()
        try:
            self.assertTrue(data == '资金状况')
            logging.info('报单查询资金的用例通过')
        except AssertionError as err:
            logging.error('报单查询资金的用例不通过')
            raise err

    def test_ReportQuery_a2_succeed(self):
        """报单查询委托的测试用例"""
        data = self.accountopening.accountname(self.data).click_weituo().get_bangdingSXF_result()
        try:
            self.assertTrue(data == '所有委托')
            logging.info('报单查询委托的用例通过')
        except AssertionError as err:
            logging.error('报单查询委托的用例不通过')
            raise err

    def test_ReportQuery_a3_succeed(self):
        """报单查询成交的测试用例"""
        data = self.accountopening.accountname(self.data).click_chengjiao().get_bangdingSXF_result()
        try:
            self.assertTrue(data == '成交明细')
            logging.info('报单查询成交的用例通过')
        except AssertionError as err:
            logging.error('报单查询成交的用例不通过')
            raise err

    def test_ReportQuery_a4_succeed(self):
        """报单查询持仓明细的测试用例"""
        data = self.accountopening.accountname(self.data).click_chicang().get_bangdingSXF_result()
        try:
            self.assertTrue(data == '持仓明细')
            logging.info('报单查询持仓明细的用例通过')
        except AssertionError as err:
            logging.error('报单查询持仓明细的用例不通过')
            raise err

    def test_ReportQuery_a5_succeed(self):
        """报单查询管理员账户资金查询的测试用例"""
        data = self.accountopening.click_facemanager().click_admin().click_zijin().get_bangdingSXF_result()
        try:
            self.assertTrue(data == '资金状况')
            logging.info('管理员账户资金查询的用例通过')
        except AssertionError as err:
            logging.error('管理员账户资金查询的用例不通过')
            raise err

    def test_ReportQuery_a6_succeed(self):
        """报单查询管理员账户委托查询的测试用例"""
        data = self.accountopening.click_weituo().get_bangdingSXF_result()
        try:
            self.assertTrue(data == '所有委托')
            logging.info('管理员账户委托查询的用例通过')
        except AssertionError as err:
            logging.error('管理员账户委托查询的用例不通过')
            raise err

    def test_ReportQuery_a7_succeed(self):
        """报单查询管理员账户成交查询的测试用例"""
        data = self.accountopening.click_chengjiao().get_bangdingSXF_result()
        try:
            self.assertTrue(data == '成交明细')
            logging.info('管理员账户成交查询的用例通过')
        except AssertionError as err:
            logging.error('管理员账户成交查询的用例不通过')
            raise err

    def test_ReportQuery_a8_succeed(self):
        """报单查询管理员账户持仓明细的测试用例"""
        data = self.accountopening.click_chicang().get_bangdingSXF_result()
        try:
            self.assertTrue(data == '持仓明细')
            logging.info('管理员账户持仓明细的用例通过')
        except AssertionError as err:
            logging.error('管理员账户持仓明细的用例不通过')
            raise err

    def test_ReportQuery_a9_succeed(self):
        """操作账户配置核算信息的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).click__SettlementManager().input_account(self.data).click_chaxun().get_chaxun_result()
        try:
            self.assertTrue(data == self.data)
            logging.info('操作账户配置核算信息的用例通过')
        except AssertionError as err:
            logging.error('操作账户配置核算信息的用例不通过')
            raise err

    def test_ReportQuery_b1_succeed(self):
        """账户历史的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).click_AccountHistoryManager().accountname(self.data).get_chaxun_result()

        try:
            self.assertTrue(data == '账户历史')
            logging.info('账户历史的用例通过')
        except AssertionError as err:
            logging.error('账户历史的用例不通过')
            raise err

    def test_ReportQuery_b2_succeed(self):
        """资金划拨的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).click_cachiomenu().variety_earnest_newly().accountname(self.data).transfer_amount()\
            .click_wancheng().window_affirm2().window_affirm2().input_product(self.data).click_shousuo().get_chaxun_result2()
        print(data)
        try:
            self.assertTrue(data['操作账户'] == self.data)
            self.assertTrue(data['总资金'] == '9,000,000')
            logging.info('资金划拨的用例通过')
        except AssertionError as err:
            logging.error('资金划拨的用例不通过')
            raise err

    def test_ReportQuery_b3_succeed(self):
        """手工行权的测试用例"""
        self.driver.refresh()
        data = IndexPage(self.driver).click_ExecorderMenu().get_result()
        print(data)
        try:
            self.assertTrue(data == '操作明细')
            logging.info('手工行权的用例通过')
        except AssertionError as err:
            logging.error('手工行权的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
