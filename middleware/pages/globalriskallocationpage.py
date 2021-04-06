import time

from common.seleniunm_packaging import BasePage


class GlobalRiskAllocation(BasePage):
    """全局风险配置页面"""
    title = '管理平台-融航商品期权资管平台'

    # 定位到追保风险度输入框
    After_confirmed = ('xpath', "//input[@id='risk']")
    # 定位到当日亏损追保线
    Of_course_loss = ('xpath', "//input[@id='risk2']")
    # 定位到最大日亏损追保比例
    Maximum_daily_loss_recovery = ('xpath', "//input[@id='risk4']")
    # 定位到强平风险度输入框
    Strong_level_of_risk = ('xpath', "//input[@id='risk1']")
    # 定位到当日亏损强平线
    day_of_losses = ('xpath', "//input[@id='risk3']")
    # 定位到最大日亏损强平比例
    Maximum_daily_loss_ratio = ('xpath', "//input[@id='risk5']")
    # 定位到总亏损追保比例
    Percentage_total_loss_recovery = ('xpath', "//input[@id='risk6']")
    # 定位到总亏损强平比例
    The_total_loss = ('xpath', "//input[@id='risk7']")
    # 定位到错误的信息
    get_error_element = ('xpath', "//div[@id='popup_message']")
    # 窗口的确认按钮
    win_queren = ('xpath', "//input[@id='popup_ok']")
    # 获取分母为市值权益
    get_market = ('xpath', "//img[@id='kzdongtai']")
    # 定位到确定按钮
    queding = ('xpath', "//input[@id='queding']")

    def input_After_confirmed(self, confirmed):
        """输入追保风险度"""
        self.find_element(self.After_confirmed).send_keys(confirmed)
        return self

    def input_course_loss(self, course):
        """输入当日亏损追保线"""
        self.find_element(self.Of_course_loss).send_keys(course)
        return self

    def input_aily_loss_recovery(self, recovery):
        """输入最大日亏损追保比例"""
        self.find_element(self.Maximum_daily_loss_recovery).send_keys(recovery)
        return self

    def input_Strong_level_risk(self, Strong):
        """输入强平风险度"""
        self.find_element(self.Strong_level_of_risk).send_keys(Strong)
        return self

    def input_day_of_losses(self, losses):
        """输入日亏损强平线"""
        self.find_element(self.day_of_losses).send_keys(losses)
        return self

    def input_Maximum_daily_loss_ratio(self, ratio):
        """输入最大日亏损强平比例"""
        self.find_element(self.Maximum_daily_loss_ratio).send_keys(ratio)
        return self

    def input_Percentage_total_loss_recovery(self, total):
        """输入总亏损追保比例"""
        self.find_element(self.Percentage_total_loss_recovery).send_keys(total)
        return self

    def input_The_total_loss(self, flat):
        """输入总亏损强平比例"""
        self.find_element(self.The_total_loss).send_keys(flat)
        return self

    def empty_message_input(self):
        """清空输入框"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.find_element(self.After_confirmed).clear()
        self.find_element(self.Of_course_loss).clear()
        self.find_element(self.Maximum_daily_loss_recovery).clear()
        self.find_element(self.Strong_level_of_risk).clear()
        self.find_element(self.day_of_losses).clear()
        self.find_element(self.Maximum_daily_loss_ratio).clear()
        self.find_element(self.Percentage_total_loss_recovery).clear()
        self.find_element(self.The_total_loss).clear()
        return self

    def get_error(self):
        """获取错误的信息"""
        el = self.find_element(self.get_error_element).text
        return el

    def win_queding(self):
        """点击窗口的确认按钮"""
        self.click(self.win_queren)
        time.sleep(1)
        return self

    def click_market(self):
        """点击分母为市值权益"""
        time.sleep(1)
        self.click(self.get_market)
        return self

    def click_queding(self):
        """点击确定按钮"""
        self.click(self.queding)
        return self
