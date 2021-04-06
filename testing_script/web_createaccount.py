"""快速创建账户并且审核出入金"""
import time
import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.accountopening import AccountOpening
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger
data = Hadnler().excel('web_customer_account_cases.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')


@ddt.ddt
class TestTheCustomerAccount(unittest.TestCase):
    """快速创建操作账户并且输入出入金"""

    @classmethod
    def setUpClass(cls) -> None:

        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        logging.info('浏览器关闭')

    @ddt.data(*data_success)
    def test_openanaccount_a1_succeed(self, test_info):
        """一键开户开户成功的用例"""
        e = 0
        while True:
            i = 'abc' + str(e)
            setattr(Hadnler, 'phone', i)
            # 创建账户
            self.accountopening.click_key_toregister_client().enter_the_name2('魏先生').enter_password2().enter_password(
                '0') \
                .account_type(Hadnler.phone).input_number(). \
                click_Margin_template().click_Commission_template(). \
                click_template().click_trading_halt().select_product1('自动化测试产品').select_risk_management('fk15'). \
                click_wancheng()
            time.sleep(1)
            # 出入输入金
            data = Hadnler.phone
            self.accountopening.operating_account_management3().input_account(data).click_search(). \
                click_operation(data).click_configuration(data).click_churujin().variety_earnest_newly() \
                .eliminate3().transfer_amount('10000000') \
                .remark_input_box('自动化测试转入的金额').variety_configuration_queding().window_affirm2().window_affirm2()
            time.sleep(1)
            # 刷新页面
            self.driver.refresh()
            if e == 100:
                break
            e += 1
            logging.info('当前创建第{}个账号'.format(i))


if __name__ == '__main__':
    unittest.main()
