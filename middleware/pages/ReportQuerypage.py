"""报单查询页面"""
import time
from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler


class ReportQuery(BasePage):
    """报单查询页面"""
    title = '管理平台-融航商品期权资管平台'


    # 定位到账号输入框
    accountname_element = ('xpath', "//input[@id='accountname']")
    # 定位到资金按钮
    zijin_element = ('xpath', "//span[text()='资金']")
    # 定位到委托按钮
    weituo_element = ('xpath',"//span[text()='委托']")
    # 定位到成交按钮
    chengjiao_element = ('xpath',"//span[text()='成交']")
    # 定位到委托按钮
    chicang_element = ('xpath',"//span[text()='持仓']")
    # 选择管理员账户
    facemanager_element = ('xpath', "//img[@id='facemanager']")
    # 选择admin
    admin_element = ('xpath', "//span[text()='admin']//preceding-sibling::label")

    def accountname(self, account):
        """输入账户名称"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.find_element(self.accountname_element).send_keys(account)
        self.click(('xpath', "//li[text()='{}']".format(account)))
        return self

    def click_zijin(self):
        """点击资金搜索按钮"""
        self.click(self.zijin_element)
        return self

    def click_weituo(self):
        """点击委托搜索按钮"""
        self.click(self.weituo_element)
        return self

    def click_chengjiao(self):
        """点击成交搜索按钮"""
        self.click(self.chengjiao_element)
        return self

    def click_chicang(self):
        """点击持仓搜索按钮"""
        self.click(self.chicang_element)
        return self

    def click_facemanager(self):
        """点击管理员账户按钮"""
        time.sleep(1)
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.facemanager_element)
        return self

    def click_admin(self):
        """点击admin"""
        time.sleep(1)
        self.click(self.admin_element)
        return self

    def get_bangdingSXF_result(self):
        """获取结果"""
        Handmore = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")
        el = self.find_element(Handmore).text
        return el