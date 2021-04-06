import unittest
import ddt as ddt
import pytest

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
    """原有客户开户"""

    @classmethod
    def setUpClass(cls) -> None:
        setattr(Hadnler, 'phone', Hadnler().mobile)
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.admin_page = IndexPage(cls.driver)
        cls.admin_page.click_existing_client().empty_message_input()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    @ddt.data(*data_error)
    def test_openanaccount_a1_error(self, test_info):
        """账户开户失败的用例"""
        logging.info('开始测试账户开户失败用例')
        data = test_info['data']
        data = Hadnler().replace_data(data)
        accountopening = AccountOpening(self.driver)
        if test_info['type'] == 2:
            actual = accountopening.enter_the_name(eval(data)['name']) \
                .enter_password(eval(test_info['data'])['password']) \
                .account_type(eval(test_info['data'])['account']).click_next() \
                .get_actual2()
            accountopening.window_affirm2().empty_message_input()
        else:
            actual = accountopening.enter_the_name(eval(data)['name']) \
                .enter_password(eval(test_info['data'])['password']) \
                .account_type(eval(test_info['data'])['account']).click_next() \
                .get_actual()
            accountopening.window_affirm().empty_message_input()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(actual == test_info['expected'])
            logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    @ddt.data(*data_success)
    def test_openanaccount_a2_succeed(self, test_info):
        """账户开户成功的用例"""
        logging.info('账户开户成功的用例')
        data = test_info['data']
        data = Hadnler().replace_data(data)
        accountopening = AccountOpening(self.driver)
        logging.info(Hadnler.name)
        actual = accountopening.enter_the_name(eval(data)['name']) \
            .enter_password(eval(test_info['data'])['password']) \
            .account_type(eval(data)['account']).click_next().futures_margin()
        logging.info('原有客户开户创建的操作账户登录账号是{}'.format(eval(data)['account']))
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(test_info['expected'] in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    def test_openanaccount_a3_succeed(self):
        """测试期货品种默认保证金率配置成功用例"""
        logging.info('开始测试期货品种默认保证金率配置成功用例')
        accountopening = AccountOpening(self.driver)
        actual = accountopening.variety_earnest_newly().variety_select().number_earnest().amount_margin_rate(). \
            variety_configuration_queding().futures_margin()

        try:
            self.assertTrue('期货品种保证金' in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    def test_openanaccount_a4_succeed(self):
        """测试期货合约默认保证金率配置成功用例"""
        logging.info('开始测试期货合约默认保证金率配置成功用例')
        accountopening = AccountOpening(self.driver)
        actual = accountopening.variety_configuration_queding().variety_earnest_newly().import_contract() \
            .number_earnest().amount_margin_rate().variety_configuration_queding().futures_margin1()
        try:
            self.assertTrue('期货合约保证金' in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    def test_openanaccount_a5_succeed(self):
        """测试品种默认手续费率配置成功的用例"""
        logging.info('测试品种默认手续费率配置成功的用例')
        accountopening = AccountOpening(self.driver)
        actual = accountopening.variety_configuration_queding().variety_earnest_newly().empty_message_input1(). \
            variety_select().shoushu_shouxufei().jine_shouxufei().variety_configuration_queding().futures_margin2()
        try:
            self.assertTrue('品种手续费' in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    def test_openanaccount_a6_succeed(self):
        """测试期货合约默认手续费率配置成功的用例"""
        logging.info('开始测试期货合约默认手续费率配置成功用例')
        accountopening = AccountOpening(self.driver)
        actual = accountopening.variety_configuration_queding().variety_earnest_newly().empty_message_input1(). \
            import_contract().shoushu_shouxufei().jine_shouxufei().variety_configuration_queding(). \
            commission_futures_Contracts()
        try:
            self.assertTrue('期货合约手续费' in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    def test_openanaccount_a7_succeed(self):
        """测试期货品种持仓限制配置成功的用例"""
        logging.info('开始测试期货品种持仓限制配置成功用例')
        accountopening = AccountOpening(self.driver)
        actual = accountopening.variety_configuration_queding().Limited_varieties().variety_select2().position_ceiling(). \
            Position_margin_limit().variety_configuration_queding().futures_position_limits()
        try:
            self.assertTrue('期货品种持仓限制' in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    def test_openanaccount_a8_succeed(self):
        """测试可交易品种/合约配置成功的用例"""
        logging.info('开始测试可交易品种/合约配置成功用例')
        accountopening = AccountOpening(self.driver)
        actual = accountopening.variety_configuration_queding().click_configuration().select_variety().click_queding() \
            .window_affirm2().get_variety_contract()
        try:
            self.assertTrue('可交易品种/合约' in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    def test_openanaccount_a9_succeed(self):
        """测试出入金配置成功的用例"""
        logging.info('开始测试出入金配置成功用例')
        accountopening = AccountOpening(self.driver)
        actual = accountopening.click_next().select_product(Hadnler.establish_company).click_next().select_pneumatic(
            Hadnler.digits).click_next(). \
            eliminate().transfer_amount().remark_input_box().click_next().window_affirm2().get_gold()
        try:
            self.assertTrue('添加待审核出入金成功！' in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    def test_openanaccount_b1_succeed(self):
        """测试断言开户成功的的用例"""
        logging.info('开始测试断言开户成功的用例')
        accountopening = AccountOpening(self.driver)
        actual = accountopening.window_affirm3().operating_account_management().input_account(
            Hadnler.phone).click_search() \
            .get_account(Hadnler().phone)
        try:
            self.assertTrue(actual == Hadnler().phone)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()

##############################快速创建########################################
#
# import unittest
# import ddt as ddt
# from middleware.heandler import Hadnler
# from middleware.pages.accountopening import AccountOpening
# from middleware.pages.homepage import IndexPage
#
# logging = Hadnler.logger
# data = Hadnler().excel('web_customer_account_cases.xlsx')
# data_error = data.read_data('error')
# data_success = data.read_data('success')
# logging.info('读取excel')
#
#
# @ddt.ddt
# class TestTheCustomerAccount(unittest.TestCase):
#     """原有客户开户"""
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         setattr(Hadnler, 'phone', Hadnler().mobile)
#         logging.info('打开浏览器')
#         cls.driver = Hadnler().login()
#         cls.admin_page = IndexPage(cls.driver)
#         cls.admin_page.click_existing_client().empty_message_input()
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.driver.quit()
#         logging.info('浏览器关闭')
#
#     # @ddt.data(*data_error)
#     # def test_openanaccount_a1_error(self, test_info):
#     #     """账户开户失败的用例"""
#     #     logging.info('开始测试账户开户失败用例')
#     #     accountopening = AccountOpening(self.driver)
#     #     if test_info['type'] == 2:
#     #         actual = accountopening.enter_the_name(eval(test_info['data'])['name']) \
#     #             .enter_password(eval(test_info['data'])['password']) \
#     #             .account_type(eval(test_info['data'])['account']).click_next() \
#     #             .get_actual2()
#     #         accountopening.window_affirm2().empty_message_input()
#     #     else:
#     #         actual = accountopening.enter_the_name(eval(test_info['data'])['name']) \
#     #             .enter_password(eval(test_info['data'])['password']) \
#     #             .account_type(eval(test_info['data'])['account']).click_next() \
#     #             .get_actual()
#     #         accountopening.window_affirm().empty_message_input()
#     #     try:
#     #         logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
#     #         self.assertTrue(actual == test_info['expected'])
#     #         logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
#     #     except AssertionError as err:
#     #         logging.error('测试用例不通过')
#     #         raise err
#
#     @ddt.data(*data_success)
#     def test_openanaccount_a2_succeed(self, test_info):
#         """账户开户成功的用例"""
#         logging.info('账户开户成功的用例')
#         data = test_info['data']
#         data = Hadnler().replace_data(data)
#         accountopening = AccountOpening(self.driver)
#         # logging.info(Hadnler.name)
#         actual = accountopening.enter_the_name('成警警') \
#             .enter_password(eval(test_info['data'])['password']) \
#             .account_type(eval(data)['account']).click_next().futures_margin()
#         logging.info('原有客户开户创建的操作账户登录账号是{}'.format(eval(data)['account']))
#         try:
#             logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
#             self.assertTrue(test_info['expected'] in actual)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#     def test_openanaccount_a3_succeed(self):
#         """测试期货品种默认保证金率配置成功用例"""
#         logging.info('开始测试期货品种默认保证金率配置成功用例')
#         accountopening = AccountOpening(self.driver)
#         actual = accountopening.variety_earnest_newly().variety_select().number_earnest().amount_margin_rate(). \
#             variety_configuration_queding().futures_margin()
#
#         try:
#             self.assertTrue('期货品种保证金' in actual)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#     def test_openanaccount_a4_succeed(self):
#         """测试期货合约默认保证金率配置成功用例"""
#         logging.info('开始测试期货合约默认保证金率配置成功用例')
#         accountopening = AccountOpening(self.driver)
#         actual = accountopening.variety_configuration_queding().variety_earnest_newly().import_contract() \
#             .number_earnest().amount_margin_rate().variety_configuration_queding().futures_margin1()
#         try:
#             self.assertTrue('期货合约保证金' in actual)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#     def test_openanaccount_a5_succeed(self):
#         """测试品种默认手续费率配置成功的用例"""
#         logging.info('测试品种默认手续费率配置成功的用例')
#         accountopening = AccountOpening(self.driver)
#         actual = accountopening.variety_configuration_queding().variety_earnest_newly().empty_message_input1(). \
#             variety_select().shoushu_shouxufei().jine_shouxufei().variety_configuration_queding().futures_margin2()
#         try:
#             self.assertTrue('品种手续费' in actual)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#     def test_openanaccount_a6_succeed(self):
#         """测试期货合约默认手续费率配置成功的用例"""
#         logging.info('开始测试期货合约默认手续费率配置成功用例')
#         accountopening = AccountOpening(self.driver)
#         actual = accountopening.variety_configuration_queding().variety_earnest_newly().empty_message_input1(). \
#             import_contract().shoushu_shouxufei().jine_shouxufei().variety_configuration_queding(). \
#             commission_futures_Contracts()
#         try:
#             self.assertTrue('期货合约手续费' in actual)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#     def test_openanaccount_a7_succeed(self):
#         """测试期货品种持仓限制配置成功的用例"""
#         logging.info('开始测试期货品种持仓限制配置成功用例')
#         accountopening = AccountOpening(self.driver)
#         actual = accountopening.variety_configuration_queding().Limited_varieties().variety_select2().position_ceiling(). \
#             Position_margin_limit().variety_configuration_queding().futures_position_limits()
#         try:
#             self.assertTrue('期货品种持仓限制' in actual)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#     def test_openanaccount_a8_succeed(self):
#         """测试可交易品种/合约配置成功的用例"""
#         logging.info('开始测试可交易品种/合约配置成功用例')
#         accountopening = AccountOpening(self.driver)
#         accountopening.variety_configuration_queding().click_next()
#
#     def test_openanaccount_a9_succeed(self):
#         """测试出入金配置成功的用例"""
#         logging.info('开始测试出入金配置成功用例')
#         accountopening = AccountOpening(self.driver)
#         actual = accountopening.select_product('自动化测试产品').click_next().select_pneumatic(
#             '88888888').click_next(). \
#             eliminate().transfer_amount().remark_input_box().click_next().window_affirm2().get_gold()
#         try:
#             self.assertTrue('添加待审核出入金成功！' in actual)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#     def test_openanaccount_b1_succeed(self):
#         """测试断言开户成功的的用例"""
#         logging.info('开始测试断言开户成功的用例')
#         accountopening = AccountOpening(self.driver)
#         actual = accountopening.window_affirm3().operating_account_management().input_account(
#             Hadnler.phone).click_search() \
#             .get_account(Hadnler().phone)
#         try:
#             self.assertTrue(actual == Hadnler().phone)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#
# if __name__ == '__main__':
#     unittest.main()
