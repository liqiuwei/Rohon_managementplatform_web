"""手工行权页面"""
from common.seleniunm_packaging import BasePage



class ExecorderMenu(BasePage):
    """手工行权页面"""
    title = '管理平台-融航商品期权资管平台'

    edittabletitle_element = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")

    def get_result(self):
        """获取到实际结果"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        el = self.find_element(self.edittabletitle_element).text
        return el



