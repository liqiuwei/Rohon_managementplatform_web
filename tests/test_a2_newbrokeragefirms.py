import unittest
import ddt as ddt
import pytest

from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage
from middleware.pages.company_Increased import EconomicsIncreased

logging = Hadnler.logger
data = Hadnler().excel('web_Additional_brokerage_firms.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')



@ddt.ddt
class TestNewlyCompany(unittest.TestCase):
    """新增经济公司"""

    @classmethod
    def setUpClass(cls) -> None:
        setattr(Hadnler, 'establish_company2', Hadnler().establish_company1())
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.admin_page = IndexPage(cls.driver)
        cls.admin_page.click_system_configuration().click_economic_administration().economics_newly()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    @ddt.data(*data_error)
    def test_company_1_error(self, test_info):
        """新增经济公司失败的用例"""
        logging.info('开始测试新增新增经纪公司失败用例')
        economicsincreased = EconomicsIncreased(self.driver)
        actual = economicsincreased.enter_company_name(eval(test_info['data'])['companyname']). \
            enter_company_code(eval(test_info['data'])['companycode']). \
            import_deal_site(eval(test_info['data'])['jiaoyifuwuqidizhi']). \
            import_market_site(eval(test_info['data'])['hangqingfuwuqidizhi']).import_result(eval(
            test_info['data'])['result']).select_counte(). \
            click_confirm().get_error()
        economicsincreased.click_wicket_confirm().empty_input()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(actual == test_info['expected'])
            logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    @ddt.data(*data_success)
    def test_company_2_succee(self, test_info):
        """新增经济公司成功的用例"""
        logging.info(Hadnler.establish_company2)
        logging.info('开始测试新增经纪公司成功用例')
        data = test_info['data']
        data = Hadnler().replace_data(data)
        expected = test_info['expected']
        expected = expected.replace('#establish_company#', eval(data)['companyname'])
        actual = self.admin_page.get().click_system_configuration().click_economic_administration().economics_newly(). \
            enter_company_name(
            eval(data)['companyname']). \
            enter_company_code(eval(test_info['data'])['companycode']). \
            import_deal_site(eval(test_info['data'])['jiaoyifuwuqidizhi']). \
            import_market_site(eval(test_info['data'])['hangqingfuwuqidizhi']).import_result(
            eval(test_info['data'])['result']) \
            .click_confirm().click_wicket_confirm().get_company_name(eval(data)['companyname'])
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(expected, actual))
            self.assertTrue(actual == expected)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
