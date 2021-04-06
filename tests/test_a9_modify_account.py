import time
import unittest
import ddt as ddt
import pytest

from middleware.heandler import Hadnler, OracleHandlerMid

from middleware.pages.homepage import IndexPage

logging = Hadnler.logger



@ddt.ddt
class TestModifyAccount(unittest.TestCase):
    """修改操作账户"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        # cls.data = '16600281508'
        cls.data = Hadnler.phone
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_modifyaccount_a1_succeed(self):
        """修改操作账户成功的用例"""
        self.accountopening.operating_account_management2().input_account(self.data).click_search(). \
            click_operation(self.data).click_configuration(self.data).click_toedit().total_positions('1') \
            .total_poscost('2').MaximumWithdrawals('3').OvernightMaginRiskRate('4').OvernightMaginRiskRate_gaoji(). \
            click_After_money().clicl_Cut_way() \
            .OVERNIGHTMARCLOSETYPE().ForceClose('5').AppendMarginRate('6').DayMaxLossNotice('7').DayMaxLossForce('8') \
            .DayMaxLossNoticeRate('9').DayMaxLossForceRate('10').Maximum().Maximum_mode().SummaryLossNoticeRatio('11') \
            .SummaryLossForceRatio('12').Total().MarginRatio('13').gaoji4().Risk_mode().Margin_allocation2(). \
            Commission_configuration() \
            .Collection_declaration().Close_exposures().realcapitalamount('14').historymaxprofit('15').Allow_policies(). \
            square_beforenight().square_dcesupporthedging().variety_configuration_queding().window_affirm2()
        time.sleep(1)
        sql = "select * from t_account t where LOGINACCOUNT='{}'".format(self.data)
        data = self.db.query2(sql, one=True)
        print(data)
        try:
            self.assertTrue(data['TOTALPOSITIONS'] == 1)
            self.assertTrue(data['TOTALPOSCOST'] == 2)
            self.assertTrue(data['MAXIMUMWITHDRAWALS'] == 3)
            self.assertTrue(data['OVERNIGHTMAGINRISKRATE'] == 0.04)
            self.assertTrue(data['FORCECLOSE'] == 5)
            self.assertTrue(data['APPENDMARGINRATE'] == 6)
            self.assertTrue(data['DAYMAXLOSSNOTICE'] == 7)
            self.assertTrue(data['DAYMAXLOSSFORCE'] == 8)
            self.assertTrue(data['DAYMAXLOSSNOTICERATE'] == 0.09)
            self.assertTrue(data['DAYMAXLOSSFORCERATE'] == 0.1)
            self.assertTrue(data['SUMMARYLOSSNOTICERATIO'] == 0.11)
            self.assertTrue(data['SUMMARYLOSSFORCERATIO'] == 0.12)
            self.assertTrue(data['MARGINRATIO'] == 0.13)
            self.assertTrue(data['REALCAPITALAMOUNT'] == 14)
            self.assertTrue(data['HISTORYMAXPROFIT'] == 15)
            self.assertTrue(data['OVERNIGHTMARDIVTYPE'] == 2)
            self.assertTrue(data['OVERNIGHTLIMITTYPE'] == 2)
            self.assertTrue(data['OVERNIGHTMARCLOSETYPE'] == 2)
            self.assertTrue(data['DAYMAXLOSSDIVTYPE'] == 3)
            self.assertTrue(data['MARGINRATIODIVTYPE'] == 2)
            self.assertTrue(data['MARGINSETTING'] == 2)
            self.assertTrue(data['COMMISSIONSETTING'] == 2)
            self.assertTrue(data['USEORDERFEE'] == 0)
            self.assertTrue(data['CLOSEIGNOREEXPOSURE'] == 1)
            self.assertTrue(data['SUPPORTHEDGE'] == 1)
            self.assertTrue(data['ISBEFORENIGHTCLOSED'] == 1)
            self.assertTrue(data['DCESUPPORTHEDGING'] == 1)
            logging.info('修改账户的测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()


# sql = "select * from t_account"
# data = OracleHandlerMid().query2(sql, one=True)
# print(data)
