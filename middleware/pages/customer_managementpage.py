"""核算信息页面"""
import time
from common.seleniunm_packaging import BasePage


class CustomerManagement(BasePage):
    """客户管理页面"""
    title = '管理平台-融航商品期权资管平台'

    # 定位到搜索框
    customename_element = ('xpath', "//input[@id='customename']")
    # 点击搜索
    sousuo_img_element = ('xpath', "//input[@class='sousuo_img']")
    # 定位到账户输入框
    accountname_element = ('xpath', "//input[@id='accountname']")
    # 定位到品种保证金的新增元素
    variety_deposit = ('xpath', "//span[text()='新增']")

    def variety_earnest_newly(self):
        """点击品种保证金的新增按钮(后面新增通用)"""
        self.click(self.variety_deposit)
        time.sleep(1)
        return self

    def input_account(self, account):
        """输入账户名称"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.find_element(self.customename_element).send_keys(account)
        return self

    def click_chaxun(self):
        """点击查询"""
        self.click(self.sousuo_img_element)
        return self

    def get_jieguo(self):
        """获取结果"""
        result_element = ('xpath', "//td[@class='table_content']//following-sibling::td")
        el = self.find_element(result_element).text
        return el

