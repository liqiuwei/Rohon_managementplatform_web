"""核算信息页面"""
import time
from common.seleniunm_packaging import BasePage


class RightsManagement(BasePage):
    """权限管理页面"""
    title = '管理平台-融航商品期权资管平台'

    # 定位到角色名称输入框
    rohon_gm_groupname_element = ('xpath', "//input[@id='rohon_gm_groupname']")
    # 定位到品种保证金的新增元素
    variety_deposit = ('xpath', "//span[text()='新增']")
    # 资金调拨员
    zijindiaoboyuan_element = ('xpath', "//img[@myvalue='zijindiaoboyuan']")
    # 定位到期货品种默认保证金率配置的确认按钮
    queding = ('xpath', "//input[@id='queding']")
    # 获取结果
    Xpath = ('xpath', "//td[contains(text(),'自动化创建的资金调拨员')]")
    # 删除
    shanchu_lement = ('xpath', "//td[contains(text(),'自动化创建的资金调拨员')]//following-sibling::td//following-sibling::td")
    # 定位到窗口的确认按钮
    queren2 = ('xpath', "//input[@id='popup_ok']")

    def window_affirm2(self):
        """确认按钮用于第一个确认无法定位到的时候"""
        self.click(self.queren2)
        return self

    def click_delete(self):
        """点击删除"""
        self.click(self.shanchu_lement)
        return self

    def isPresent2(self):
        """判断元素是否存在"""
        try:
            self.find_element(self.Xpath)
        except Exception as err:
            return False
        return True

    def variety_configuration_queding(self):
        """点击确定"""
        time.sleep(1)
        self.click(self.queding)
        return self

    def click_zijindiaoboyuan(self):
        """点击资金调拨员工"""
        self.click(self.zijindiaoboyuan_element)
        return self

    def click_rohon_gm_groupname(self):
        """输入角色名称"""
        self.find_element(self.rohon_gm_groupname_element).send_keys('自动化创建的资金调拨员')
        return self

    def variety_earnest_newly(self):
        """点击品种保证金的新增按钮(后面新增通用)"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.variety_deposit)
        time.sleep(1)
        return self

    def get_jieguo(self):
        """获取结果"""
        result_element = ('xpath', "//td[@class='table_content']//following-sibling::td")
        el = self.find_element(result_element).text
        return el

