import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger
data = Hadnler().excel('web_Additional_brokerage_firms.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')


@ddt.ddt
class TestAuditPayment(unittest.TestCase):
    """审核出入金"""

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('打开浏览器')
        cls.driver = Hadnler().login(Hadnler.login_account, '李秋维的资金账户')
        cls.bank_treasurer_login = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_review_money_1_succee(self):
        """审核入金成功得用例"""
        logging.info('登录成功开始测试审核出入金成功得用例')
        actual1 = self.bank_treasurer_login.click_money_affirm2().click_audit_queren().result()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format('出入金成功', actual1))
            self.assertTrue(actual1 == '出入金成功')
            logging.info('入金审核通过')
        except AssertionError as err:
            logging.error('入金审核不通过')
            raise err

    def test_review_money_2_succee(self):
        """审核出金成功得用例"""
        logging.info('登录成功开始测试审核出入金成功得用例')
        actual2 = self.bank_treasurer_login.click_audit_queren().click_money_affirm().click_audit_queren().result()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format('出入金成功', actual2))
            self.assertTrue(actual2 == '出入金成功')
            logging.info('出金审核通过')
        except AssertionError as err:
            logging.error('出金审核不通过')


if __name__ == '__main__':
    unittest.main()
