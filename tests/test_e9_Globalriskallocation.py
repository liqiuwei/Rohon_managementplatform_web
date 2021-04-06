# import unittest
# import ddt as ddt
#
# from common.Oracle_packaging import OracleHandler
#
# from middleware.pages.globalriskallocationpage import GlobalRiskAllocation
# from middleware.pages.homepage import IndexPage
# from middleware.heandler import OracleHandlerMid
# from middleware.heandler import Hadnler
#
# logging = Hadnler.logger
# data = Hadnler().excel('web_Global_risk_allocation_cases.xlsx')
# data_error = data.read_data('error')
# data_success = data.read_data('success')
# logging.info('读取excel')
#
#
# @ddt.ddt
# class TestGlobalRiskAllocation(unittest.TestCase):
#     """全局风险度配置"""
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.ab = OracleHandlerMid()
#         setattr(Hadnler, 'confirmed', Hadnler().figure_max)
#         setattr(Hadnler, 'Strong', Hadnler().figure_min)
#         setattr(Hadnler, 'course', Hadnler().figure_min)
#         setattr(Hadnler, 'losses', Hadnler().figure_max)
#         setattr(Hadnler, 'recovery', Hadnler().figure_min)
#         setattr(Hadnler, 'ratio', Hadnler().figure_max)
#         setattr(Hadnler, 'total', Hadnler().figure_min)
#         setattr(Hadnler, 'flat', Hadnler().figure_max)
#         logging.info('打开浏览器')
#         cls.driver = Hadnler().login()
#         cls.admin_page = IndexPage(cls.driver)
#         cls.admin_page.click_risk_control_allocation().click_Office_risk_allocation()
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.driver.quit()
#         logging.info('浏览器关闭')
#         cls.ab.close()
#
#     @ddt.data(*data_error)
#     def test_Risk_allocation_a1_error(self, test_info):
#         """全局风险度配置失败得用例"""
#         logging.info('开始测试添全局风险度配置失败的用例')
#         globalriskallocation = GlobalRiskAllocation(self.driver)
#         if test_info['type'] == 2:
#             actual = globalriskallocation.empty_message_input().input_After_confirmed(
#                 eval(test_info['data'])['confirmed']). \
#                 input_Strong_level_risk(eval(test_info['data'])['Strong']).input_course_loss(
#                 eval(test_info['data'])['course']) \
#                 .input_day_of_losses(eval(test_info['data'])['losses']).input_aily_loss_recovery(
#                 eval(test_info['data'])['recovery']). \
#                 input_Maximum_daily_loss_ratio(eval(test_info['data'])['ratio']) \
#                 .input_Percentage_total_loss_recovery(eval(test_info['data'])['total']).input_The_total_loss(
#                 eval(test_info['data'])['flat']). \
#                 input_After_confirmed(eval(test_info['data'])['confirmed']).get_error()
#         else:
#             actual = globalriskallocation.empty_message_input().input_After_confirmed(
#                 eval(test_info['data'])['confirmed']). \
#                 input_Strong_level_risk(eval(test_info['data'])['Strong']).input_course_loss(
#                 eval(test_info['data'])['course']) \
#                 .input_day_of_losses(eval(test_info['data'])['losses']).input_aily_loss_recovery(
#                 eval(test_info['data'])['recovery']). \
#                 input_Maximum_daily_loss_ratio(eval(test_info['data'])['ratio']) \
#                 .input_Percentage_total_loss_recovery(eval(test_info['data'])['total']).input_The_total_loss(
#                 eval(test_info['data'])['flat']).get_error()
#         try:
#             logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
#             self.assertTrue(test_info['expected'] == actual)
#             logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#     @ddt.data(*data_success)
#     def test_Risk_allocation_a2_success(self, test_info):
#         """全局风险度配置成功用例"""
#         logging.info('开始测试添全局风险度配置成功的用例')
#         data = test_info['data']
#         data = Hadnler().replace_data(data)
#         globalriskallocation = IndexPage(self.driver)
#         globalriskallocation.click_Office_risk_allocation2().empty_message_input().input_After_confirmed(
#             eval(data)['confirmed']). \
#             input_Strong_level_risk(eval(data)['Strong']).input_course_loss(eval(data)['course']) \
#             .input_day_of_losses(eval(data)['losses']).input_aily_loss_recovery(eval(data)['recovery']). \
#             input_Maximum_daily_loss_ratio(eval(data)['ratio']).input_Percentage_total_loss_recovery(
#             eval(data)['total']) \
#             .input_The_total_loss(eval(data)['flat']).click_queding().win_queding()
#
#         data = self.ab.query2("select * from t_riskctralparam t")
#
#         try:
#             logging.info('预期结果:{}，实际结果:{}'.format(Hadnler.confirmed, str(data[0]['NEEDAPPENDMARGIN'])))
#             self.assertTrue(str(data[0]['NEEDAPPENDMARGIN']) == Hadnler.confirmed)
#             self.assertTrue(str(data[0]['NEEDFORCECLOSE']) == Hadnler.Strong)
#             self.assertTrue(str(data[0]['DAYMAXLOSSNOTICE']) == Hadnler.course)
#             self.assertTrue(str(data[0]['DAYMAXLOSSFORCE']) == Hadnler.losses)
#             logging.info('测试用例通过')
#         except AssertionError as err:
#             logging.error('测试用例不通过')
#             raise err
#
#
# if __name__ == '__main__':
#     unittest.main()
