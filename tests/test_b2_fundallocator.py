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
    """创建资金调拨员账户"""

    def setUp(self) -> None:
        setattr(Hadnler, 'login_account', Hadnler().Nine_digits)
        logging.info('打开浏览器')
        self.data = Hadnler.one__key_phone
        # self.data = '13887423140'
        self.driver = Hadnler().login()
        self.admin_page = IndexPage(self.driver)
        self.NewAdministrator = self.admin_page.click_system_configuration().login_account_newly()

    def tearDown(self) -> None:
        self.driver.quit()
        logging.info('浏览器关闭')

    def test_audit_payment_1_succee(self):
        """创建资金调拨员成功得用例"""
        logging.info('开始创建资金调拨员成功得用例')
        actual = self.NewAdministrator.input_name(Hadnler.login_account).input_pwd('李秋维的资金账户').click_allot()\
            .click_Check_the_account().select_operating_account(self.data).click_queding().\
            click_winqueding().input_account(Hadnler.login_account).click_search().get_results(Hadnler.login_account)
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(Hadnler.login_account, actual))
            self.assertTrue(actual == Hadnler.login_account)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
