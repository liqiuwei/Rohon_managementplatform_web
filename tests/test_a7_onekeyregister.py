import unittest
import ddt as ddt
import pytest

from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger
data = Hadnler().excel('web_customer_account_cases.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')



@ddt.ddt
class TestTheCustomerAccount(unittest.TestCase):
    """一键开户"""

    @classmethod
    def setUpClass(cls) -> None:
        setattr(Hadnler, 'one__key_phone', Hadnler().mobile)
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    # @ddt.data(*data_success)
    def test_openanaccount_a1_succeed(self):
        """一键开户开户成功的用例"""

        logging.info('测试一键开户开户成功的用例')
        actual = self.accountopening.click_key_toregister_client().enter_the_name2(
            '李秋维').enter_password2().enter_password('0') \
            .account_type(Hadnler.one__key_phone).input_number(). \
            click_Margin_template().click_Commission_template(). \
            click_template().click_trading_halt().select_product1(Hadnler().establish_company).select_risk_management(
            Hadnler().digits). \
            click_wancheng().operating_account_management().input_account(
            Hadnler.one__key_phone).click_search().get_account(Hadnler.one__key_phone)
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(Hadnler.one__key_phone, actual))
            self.assertTrue(Hadnler.one__key_phone in actual)
            logging.info('一键开户创建的账户是{}'.format(Hadnler.one__key_phone))
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()

# ######################循环创建账户脚本##########################################
# @ddt.ddt
# class TestTheCustomerAccount(unittest.TestCase):
#     """一键开户"""
#
#     @classmethod
#     def setUpClass(cls) -> None:
#
#         logging.info('打开浏览器')
#         cls.driver = Hadnler().login()
#         cls.accountopening = IndexPage(cls.driver)
#
#     # @classmethod
#     # def tearDownClass(cls) -> None:
#     #     cls.driver.quit()
#     #     logging.info('浏览器关闭')
#
#     @ddt.data(*data_success)
#     def test_openanaccount_a1_succeed(self, test_info):
#         """一键开户开户成功的用例"""
#         i = 0
#         while True:
#             try:
#                 setattr(Hadnler, 'phone', Hadnler().mobile)
#                 # logging.info('账户开户成功的用例')
#                 data = test_info['data']
#                 data = Hadnler().replace_data(data)
#
#                 self.accountopening.click_key_toregister_client().enter_the_name2('魏先生').enter_password2().enter_password('0') \
#                     .account_type(eval(data)['account']).input_number().\
#                     click_Margin_template().click_Commission_template(). \
#                     click_template().click_trading_halt().select_product1('产品1').select_risk_management('FK'). \
#                     click_wancheng()
#                 time.sleep(1)
#                 self.driver.refresh()
#                 if i == 3000:
#                     break
#                 i += 1
#                 logging.info('当前创建第{}个账号'.format(i))
#             except  Exception as err:
#                 logging.info('没有找到元素')


#
# if __name__ == '__main__':
#     unittest.main()
