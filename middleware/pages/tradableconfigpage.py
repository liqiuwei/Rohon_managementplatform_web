import time
from common.seleniunm_packaging import BasePage


class TradableConfig(BasePage):
    """全局可交易品种/合约页面"""
    title = '管理平台-融航商品期权资管平台'
    # 定位到品种合约的配置按钮
    configuration = ('xpath', "//a[@onclick=' add()']")
    # 定位ag品种选择框
    pinzong = ('xpath', "//img[@id='product_ag']")
    # 定位bu品种>箭头框
    bu2 = ('xpath', "//img[@id='selectImg_bu']")
    # 定位bu下的主力按钮
    bu_zhuli = ('xpath', "//img[@myvalue='bu主力']")
    # 定位bu下的次主力
    bu_cizhuli = ('xpath', "//img[@myvalue='bu次主力']")
    # 定位到bu下的主力三
    bu_zhulisan = ('xpath', "//img[@myvalue='bu主力三']")
    # 定位品种选择的确认按钮
    queding = ('xpath', "//input[@id='queding' and @class='addSub']")
    # 定位弹框的确认按钮
    win_queren = ('xpath', "//input[@id='popup_ok']")
    # 获取到成功的结果
    actual =  ('xpath', "//div[@id='popup_message']")
    # 获取到全选按钮
    check = ('xpath', "//img[@class='quanxuanF quanxuanC']")
    # 定位到删除按钮
    det = ('xpath', "//span[text()='删除']")

    def click_config(self):
        """点击配置按钮（品种合约配置）"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.configuration)
        return TradableConfig(self.driver)

    def click_ag(self):
        """点击ag品种"""
        self.click(self.pinzong)
        return self

    def click_bu2(self):
        """点击bu品种的>箭头"""
        time.sleep(1)
        self.click(self.bu2)

        return self

    def click_bu_zhuli(self):
        """点击bu下的主力"""
        time.sleep(2)
        self.click(self.bu_zhuli)
        return self

    def click_bu_cizhuli(self):
        """点击bu下的次主力"""
        self.click(self.bu_cizhuli)
        return self

    def click_bu_zhulisan(self):
        """点击bu下的主力三"""
        self.click(self.bu_zhulisan)
        return self

    def clicl_queding(self):
        """点击品种选择的确认按钮"""
        self.click(self.queding)
        return self

    def clicl_win_queren(self):
        """点击小窗口的确认按钮"""
        self.click(self.win_queren)
        return self

    def get_actual(self):
        """获取到成功的文本"""
        time.sleep(1)
        el = self.find_element(self.actual).text
        return el

    def click_check(self):
        """点击全选按钮"""
        self.click(self.check)
        return self

    def click_del(self):
        """点击删除按钮"""
        self.click(self.det)
        return self