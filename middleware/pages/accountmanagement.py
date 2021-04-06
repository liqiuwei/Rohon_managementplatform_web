import time

from common.seleniunm_packaging import BasePage



class AccountManagement(BasePage):
    """操作作账户管理页面"""
    title = '管理平台-融航商品期权资管平台'
    # 搜索输入框
    Search_input_box = ('xpath', "//input[@class='sousuo_button ac_input']")
    # 搜索按钮
    search = ('xpath', "//input[@class='sousuo_img']")

    def input_account(self, account):
        """搜索框输入账户"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.Situation_box(self.Search_input_box)
        self.find_element(self.Search_input_box).send_keys(account)
        return self

    def click_search(self):
        "点击搜索按钮"
        self.click(self.search)
        return self

    def get_account(self, account):
        """获取到新添加成功的账户"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        account_element = ('xpath', "//td[contains(text(),'{}')]".format(account))
        time.sleep(1)
        el = self.find_element(account_element).text
        return el

    def click_operation(self, account):
        """点击操作按钮"""
        account_element = ('xpath', "//td[contains(text(),'{}')]//following-sibling::td//li[text()='操作']".format(account))
        self.click(account_element)
        return self

    def click_configuration(self, account):
        """点击配置"""
        from middleware.pages.account_configurationpage import AccountConfiguration
        configuration_element = ('xpath', "//td[contains(text(),'{}')]//following-sibling::td//a[text()='配置']".format(account))
        self.click(configuration_element)
        return AccountConfiguration(self.driver)
