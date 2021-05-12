import unittest
import ddt as ddt
import pytest

from middleware.heandler import Hadnler, OracleHandlerMid
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger



@ddt.ddt
class TestSettingFundst(unittest.TestCase):
    """账户出入金设置"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = OracleHandlerMid()
        logging.info('打开浏览器')
        cls.data = Hadnler.one__key_phone
        # cls.data = '16600281508'
        cls.driver = Hadnler().login()
        cls.accountopening = IndexPage(cls.driver).operating_account_management2().input_account(cls.data).click_search(). \
            click_operation(cls.data).click_configuration(cls.data).click_churujin()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    def test_settingfundst_a1_succeed(self):
        """出入金转入的用例"""
        data = self.accountopening.variety_earnest_newly().churujingaoji()\
            .eliminate2().transfer_amount().CREDIT_amount()\
            .remark_input_box('自动化测试转入的金额').variety_configuration_queding().window_affirm2().window_affirm2().zhuanru_jine()

        data2 = self.accountopening.zhuanru_jine2()
        try:
            self.assertTrue(data == '9,000,000')
            self.assertTrue(data2 == '1,000,000')
            logging.info('出入金转入的用例用例通过')
        except AssertionError as err:
            logging.error('出入金转入的用例用例不通过')
            raise err

    def test_settingfundst_a2_succeed(self):
        """出入金转出的用例"""
        data = self.accountopening.variety_earnest_newly().churujinxuanze().chujin_zhuanchu().churujingaoji()\
            .eliminate2().transfer_amount('10000').CREDIT_amount('1000')\
            .remark_input_box('自动化测试转入的金额').variety_configuration_queding().window_affirm2().window_affirm2().zhuanru_jine()
        data2 = self.accountopening.zhuanru_jine2()
        try:
            self.assertTrue(data == '10,000')
            self.assertTrue(data2 == '1,000')
            logging.info('出入金转出的用例用例通过')
        except AssertionError as err:
            logging.error('出入金转出的用例用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()


# sql = "select * from t_account"
# data = OracleHandlerMid().query2(sql, one=True)
# print(data)
