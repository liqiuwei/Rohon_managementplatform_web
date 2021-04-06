# import time
#
# from middleware.pages.Trading_side import TradingSide
# import unittest
# import ddt as ddt
# from middleware.heandler import Hadnler, OracleHandlerMid
#
# logging = Hadnler.logger
#
# @ddt.ddt
# class TestCancellations(unittest.TestCase):
#     """客户端撤单"""
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.account_data = Hadnler().get_operation_account
#         cls.name_data = Hadnler().get_registrant
#         cls.db = OracleHandlerMid()
#         cls.client = TradingSide(path='RHClient.exe').login(cls.account_data, '0').switching_window(
#             account=cls.account_data, name='李秋维')
#         cls.sum = cls.client.unsettled_sum()
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.client.close_client()
#         cls.db.close()
#         logging.info('客户端关闭')
#
#     def test_order_unsettled_a1_success(self):
#         """客户端报单未成交状态"""
#         logging.info('开始测试客户端报单成功得用例')
#         actual = self.client.input_contract('cu2011').select_deal('买入').input_price('48000').input_Number(
#             '1').click_place().click_affirm().unsettled_sum()
#         setattr(Hadnler, 'order_ticket', actual)
#         time.sleep(1)
#         # 查询报单的数据库
#         customs_sq = "select * from t_orderdetail t where INVESTORID='{}' order by INSERTDATE DESC ,INSERTTIME desc".format(self.account_data)
#         customs_data = self.db.query2(customs_sq, True)
#         try:
#             # 未成交记录总数
#             self.assertTrue(self.sum + 1 == actual)
#             # 买卖方向
#             self.assertTrue(customs_data['DIRECTION'] == '0')
#             # 价格
#             self.assertTrue(str(customs_data['LIMITPRICE']) == '48000')
#             # 报单状态
#             self.assertTrue(customs_data['ORDERSTATUS'] == '3')
#             # 数量
#             self.assertTrue(str(customs_data['VOLUMETOTALORIGINAL']) == '1')
#             logging.info('客户端报单未成交用例通过')
#         except AssertionError as err:
#             logging.error('客户端报单未成交用例不通过')
#             raise err
#
#     def test_order_unsettled_a2_success(self):
#         """客户端撤单"""
#         logging.info('开始测客户端撤单得用例')
#         actual = self.client.Choose_from_single().unsettled_sum()
#         # 查询报单的数据库
#         customs_sq = "select * from t_orderdetail t where INVESTORID='{}' order by INSERTDATE DESC ,INSERTTIME desc".format(self.account_data)
#         customs_data = self.db.query2(customs_sq, True)
#         time.sleep(1)
#         try:
#             # 未成交记录总数
#             self.assertTrue(Hadnler.order_ticket - 1 == actual)
#             # 买卖方向
#             self.assertTrue(customs_data['DIRECTION'] == '0')
#             # 价格
#             self.assertTrue(customs_data['LIMITPRICE'] == 48000)
#             # 报单状态
#             self.assertTrue(customs_data['ORDERSTATUS'] == '5')
#             # 数量
#             self.assertTrue(str(customs_data['VOLUMETOTALORIGINAL']) == '1')
#             logging.info('客户端撤单用例通过')
#         except AssertionError as err:
#             logging.error('客户端撤单用例不通过')
#             raise err
#
#
# if __name__ == '__main__':
#     unittest.main()
#
