import time
import unittest
import ddt as ddt
from middleware.heandler import Hadnler
from middleware.pages.homepage import IndexPage

logging = Hadnler.logger
data = Hadnler().excel('web_Opening_permission_template_cases.xlsx')
data_error = data.read_data('error')
data_success = data.read_data('success')
logging.info('读取excel')


@ddt.ddt
class TestMarginRate(unittest.TestCase):
    """保证金率模版新增"""

    @classmethod
    def setUpClass(cls) -> None:
        setattr(Hadnler, 'templat_name', Hadnler().template_name)
        logging.info('打开浏览器')
        cls.driver = Hadnler().login()
        cls.admin_page = IndexPage(cls.driver)
        cls.MarginRateTemplate = cls.admin_page.click_template2().click_margin_rate()
        cls.MarginRateTemplate.new_capital_account()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logging.info('浏览器关闭')

    @ddt.data(*data_error)
    def test_varietiespermissions_a1_error(self, test_info):
        """保证金率模版新增失败的用例"""
        logging.info('开始测试品种开仓权限模板新增失败的用例')
        actual = self.MarginRateTemplate.input_template_name(eval(test_info['data'])['name'])\
                .click_queding().get_actual()
        self.MarginRateTemplate.empty_input().click_win_queding()

        try:
            logging.info('预期结果:{}，实际结果:{}'.format(test_info['expected'], actual))
            self.assertTrue(actual == test_info['expected'])
            logging.info('测试品种开仓权限模板新增失败的用例通过')
        except AssertionError as err:
            logging.error('测试品种开仓权限模板新增失败的用例不通过')
            raise err

    @ddt.data(*data_success)
    def test_varietiespermissions_a2_success(self, test_info):
        """保证金率模版新增成功的用例"""
        logging.info('开始测试品种开仓权限模板新增成功的用例')
        data = test_info['data']
        data = Hadnler().replace_data(data)
        self.MarginRateTemplate.input_template_name(eval(data)['name']) \
            .click_queding().click_operation(eval(data)['name']).click_collocate().variety_earnest_newly().empty_input2().\
            variety_select().number_earnest().amount_margin_rate().click_queding()
        time.sleep(1)
        try:
            self.assertTrue(self.MarginRateTemplate.isPresent("//td[@id='TF']"))
            self.assertTrue(self.MarginRateTemplate.isPresent("//td[@value='200.0']"))
            self.assertTrue(self.MarginRateTemplate.isPresent("//td[@value='30.0']"))
            logging.info('测试保证金率模版新增成功的用例通过')
        except AssertionError as err:
            logging.error('测试保证金率模版新增成功的用例不通过')
            raise err

    def test_varietiespermissions_a3_success(self):
        """保证金率模版新增成功的用例"""
        logging.info('开始测试保证金率模版新增成功的用例')
        self.MarginRateTemplate.click_contract_rate().empty_input2().import_contract().number_earnest().\
            amount_margin_rate().click_queding()
        time.sleep(1)
        try:
            self.assertTrue(self.MarginRateTemplate.isPresent("//td[@id='{}']".format(Hadnler.yaml['contract'])))
            logging.info('测试保证金率模版新增成功的用例通过')
        except AssertionError as err:
            logging.error('测试保证金率模版新增成功的用例不通过')
            raise err


if __name__ == '__main__':
    unittest.main()
