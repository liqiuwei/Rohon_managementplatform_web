# import time
# from middleware.pages.Trading_side import TradingSide
# import unittest
# import ddt as ddt
# from middleware.heandler import Hadnler, OracleHandlerMid
#
# logging = Hadnler.logger
#
#
# @ddt.ddt
# class TestOrder(unittest.TestCase):
#     """客户端报单"""
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.account_data = Hadnler().get_operation_account
#         # cls.account_data = '13667273351'
#         cls.client = TradingSide(path='RHClient.exe').login(cls.account_data, '0').switching_window(
#             account=cls.account_data, name='李秋维')
#         cls.data = cls.client.get_All_entrust()
#         # cls.name_data = Hadnler().get_registrant
#         cls.db = OracleHandlerMid()
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.client.close_client()
#         cls.db.close()
#         time.sleep(4)
#         logging.info('客户端关闭')
#
#     def test_order_a1_success(self):
#         """客户端报单(买入)"""
#         logging.info('开始测试客户端报单成功得用例')
#         actual = self.client.input_contract('cu2011').select_deal('买入').click_With_assign().input_Number(
#             '1').click_place().click_affirm().click_With_disk().get_All_entrust()
#         time.sleep(1)
#         # 查询报单的数据库
#         customs_sq = "select * from t_orderdetail t where INVESTORID='{}' order by INSERTDATE DESC ,INSERTTIME desc".format(
#             self.account_data)
#         customs_data = self.db.query2(customs_sq, True)
#         # 查询成交成功的数据库
#         make_sq = "select * from t_tradedetail t where INVESTORID='{}' order by TRADEDATE DESC ,TRADETIME desc".format(
#             self.account_data)
#         make_data = self.db.query2(make_sq, True)
#         try:
#             self.assertTrue(self.data + 1 == actual)
#             self.assertTrue(customs_data['STATUSMSG'] == '报单全部成交')
#             # 报单价格大于成交价格
#             self.assertTrue(customs_data['LIMITPRICE'] >= make_data['TRADEPRICE'])
#             # 买卖方向
#             self.assertTrue(make_data['DIRECTION'] == '0')
#             # 手数
#             self.assertTrue(str(make_data['VOLUME']) == '1')
#             logging.info('客户端报单成功的用例通过')
#         except AssertionError as err:
#             logging.error('客户端报单成功的用例不通过')
#             raise err
#
#     def test_order_a2_success(self):
#         """客户端报单(卖出)"""
#         logging.info('开始测试客户端报单成功得用例')
#         front_actual = self.client.get_Position_number()
#         queen_actual = self.client.sale_position().click_affirm().get_Position_number()
#         time.sleep(1)
#         # 查询报单的数据库
#         customs_sq = "select * from t_orderdetail t where INVESTORID='{}' order by INSERTDATE DESC ,INSERTTIME desc".format(
#             self.account_data)
#         customs_data = self.db.query2(customs_sq, True)
#         # 查询成交成功的数据库
#         make_sq = "select * from t_tradedetail t where INVESTORID='{}' order by TRADEDATE DESC ,TRADETIME desc".format(
#             self.account_data)
#         make_data = self.db.query2(make_sq, True)
#         try:
#             self.assertTrue(front_actual - 1 == queen_actual)
#             # 买卖方向
#             self.assertTrue(make_data['DIRECTION'] == '1')
#             # 手数
#             self.assertTrue(str(make_data['VOLUME']) == '1')
#             # 开平方向
#             self.assertTrue(str(make_data['OFFSETFLAG']) == '3')
#             logging.info('客户端报单成功的用例通过')
#         except AssertionError as err:
#             logging.error('客户端报单成功的用例不通过')
#             raise err
#
#
# if __name__ == '__main__':
#     unittest.main()
