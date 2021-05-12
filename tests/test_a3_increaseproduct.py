import unittest
import ddt as ddt
import pytest

from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage
from middleware.pages.product import IncreaseProduct

logging = Hadnler.logger
data = Hadnler().excel('web_new_product_cases.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')


@ddt.ddt
class TestNewProduct(unittest.TestCase):
    """新增产品"""

    @classmethod
    def setUpClass(cls) -> None:
        setattr(Hadnler, 'establish_company', Hadnler().establish_company1())
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.admin_page = IndexPage(cls.driver)
        cls.admin_page.click_capital_account_allocation().click_product_admin().click_new_product()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    @ddt.data(*data_error)
    def test_newlyproduct_1_error(self, test_info):
        """新增产品失败的用例"""
        logging.info('开始测试新增新增产品失败用例')
        increaseproduct = IncreaseProduct(self.driver)
        data = eval(test_info['data'])['product']
        if data == "#李秋维的产品#":
            data = data.replace("#李秋维的产品#", Hadnler().establish_company)
        actual = increaseproduct.import_product_name(data).import_product_alias(eval(test_info['data'])['alias']). \
            click_queren().get_error()
        increaseproduct.click_window_queding().empty_message_input()
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(actual == test_info['expected'])
            logging.info('第{}条失败测试用例通过'.format(test_info['case_id']))
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err

    @ddt.data(*data_success)
    def test_newlyproduct_2_succeed(self, test_info):
        """新增产品成功的用例"""
        logging.info('开始测试新增产品成功用例')
        increaseproduct = IncreaseProduct(self.driver)
        data = test_info['data']
        data = Hadnler().replace_data(data)
        expected = test_info['expected']
        expected = expected.replace('#新增的产品名称#', eval(data)['product'])
        actual = increaseproduct.import_product_name(eval(data)['product']).import_product_alias(
            eval(test_info['data'])['alias']).select_order_way().click_queren().input_product(
            Hadnler.establish_company).click_search() \
            .get_company_name(eval(data)['product'])
        try:
            logging.info('预期结果:{}，实际结果:{}'.format(expected, actual))
            self.assertTrue(expected in actual)
            logging.info('测试用例通过')
        except AssertionError as err:
            logging.error('测试用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
