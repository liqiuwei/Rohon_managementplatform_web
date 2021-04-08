"""产品管理页面"""
import time

from selenium.webdriver.support.select import Select
from common.seleniunm_packaging import BasePage


class GroupMenu(BasePage):
    """产品管理页面"""
    title = '管理平台-融航商品期权资管平台'
    # 点击产品编辑
    DailyCheckReport_element = ('xpath', "//a[@id='_DailyCheckReport']")
    # 产品别名
    synonymname_element = ('xpath', "//input[@id='synonymname']")
    # 最大可绑定资金账户数量
    oldrealaccountNum_element = ('xpath', "//input[@id='oldrealaccountNum']")
    # 最大可绑定操作账户数量
    accountNum_element = ('xpath', "//input[@id='accountNum']")
    # 定位完成按钮
    wancheng = ('xpath', "//input[@id='queding']")
    # 定位获取结果元素
    actual_result = ('xpath', "//div//div[@id='popup_message']")
    # 风控方案配置
    fkfacp1_element = ('xpath', "//a[text()='风控方案配置']")
    # 新增
    newly_element = ('xpath', "//span[text()='新增']")
    # 风控方案名称输入框
    RiskPlanName_element = ('xpath',"//input[@id='RiskPlanName']")
    # 定位到全选按钮
    quanxuan_element = ('xpath', "//img[@class='quanxuan']")
    # 批量删除
    positionschecks_element = ('xpath', "//span[text()='批量删除']")
    # 定位到窗口的确认按钮
    queren2 = ('xpath', "//input[@id='popup_ok']")
    # 定位到风控区间
    fkqjcp1_element = ('xpath', "//a[text()='风控区间配置']")
    # 定位到增加区间
    zengjiaqujian_element = ('xpath', "//span[text()='增加区间']")
    #定位到风控方案选择框
    btn_select1 = ('xpath', "//div[@id='btn-select1']")
    # 定位预警线
    yujingxian = ('xpath', "//div[text()='预警线']")
    # 定位到净值输入框
    net_worth = ('xpath', "//input[@myname='myname1']")
    # 定位到早盘交易品种
    zaopan1_element = ('xpath', "//a[@id='zaopan1']")
    # 定位到夜盘交易品种
    yepan1_element = ('xpath', "//a[text()='夜盘交易品种']")
    # 定位到配置按钮
    configuration = ('xpath', "//span[text()='配置']")
    # 定位到操作账户期货可交易品种/合约配置的ag
    ag_element = ('xpath', "//img[@id='product_ag']")
    # 定位到操作账户期货可交易品种/合约配置的ag
    quanxuanF_quanxuanC_element = ('xpath', "//img[@class='quanxuanF quanxuanC']")
    # 定位到删除按钮
    shanchu3_element = ('xpath', "//span[text()='删除']")
    # 定位到当月交割品种
    DYJG2_element = ('xpath', "//a[text()='当月交割品种']")
    # 定位到平今转开仓
    CTO1_element = ('xpath', "//a[text()='平今转开仓']")
    # 定位到板块管理
    bankuaicp_element = ('xpath', "//a[text()='板块管理']")
    # 搜索输入框
    Search_input_box = ('xpath', "//input[@class='sousuo_button ac_input']")
    # 搜索按钮
    search = ('xpath', "//input[@class='sousuo_img']")
    # 费用查询
    feiyong_element = ('xpath', "//span[text()='费用查询']")
    # 外部报单配置
    waibubaodancp2_element = ('xpath', "//a[contains(text(),'外部报单配置')]")
    # 品种交易模式
    _DailyCheckReport_element = ('xpath', "//a[contains(text(),'品种交易模式')]")
    # 定位到品种id选择框
    variety_select_element = ('xpath', "//select[@id='grouptradecontrol.productid']")
    # 产品总结报告
    DailyCheckReport2_element = ('xpath', "//a[contains(text(),'产品总结报告')]")
    # 估值文件上传
    guzhishangchuan_element = ('xpath', "//span[contains(text(),'估值文件上传')]")
    # 估值文件日期
    tradingday_element = ('xpath', "//input[@id='tradingday']")
    # 点击文件上传
    myFile_element = ('xpath', "//input[@id='myFile']")

    def click_feiyong(self):
        """点击费用查询"""
        self.click(self.feiyong_element)
        return self

    def click_myFile(self):
        """点击点击文件上传"""
        self.find_element(self.myFile_element).send_keys(r'C:\估值文件上传.xlsx')
        return self

    def click_guzhishangchuan(self):
        """点击点击文件上传"""
        self.click(self.guzhishangchuan_element)
        return self

    def click_DailyCheckReport2(self):
        """点击产品总结报告"""
        self.click(self.DailyCheckReport2_element)
        return self

    def click_DailyCheckReport(self):
        """点击品种交易模式"""
        self.click(self._DailyCheckReport_element)
        return self

    def click_waibubaodancp2(self):
        """点击费用管理"""
        self.click(self.waibubaodancp2_element)
        return self

    def click_bankuaicp(self):
        """点击板块管理"""
        self.click(self.bankuaicp_element)
        return self

    def input_product(self, account):
        """搜索框输入产品"""
        time.sleep(1)
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.find_element(self.Search_input_box).send_keys(account)
        return self

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.search)
        time.sleep(1)
        return self

    def click_CTO1(self):
        """点击平今转开仓"""
        self.click(self.CTO1_element)
        return self

    def exchange_CFFEX(self):
        """选择品种停板交易权限品种选择的中国金融交易所"""
        exchange_CFFEX_element = ('xpath', "//img[@id='exchange_CFFEX']")
        self.click(exchange_CFFEX_element)
        return self

    def click_DYJG2(self):
        """点击当月交割品种"""
        self.click(self.DYJG2_element)
        return self

    def shanchu3(self):
        """点击删除按钮"""
        self.click(self.shanchu3_element)
        return self

    def click_quanxuan2(self):
        """点击全选按钮"""
        self.click(self.quanxuanF_quanxuanC_element)
        return self

    def click_ag(self):
        """点击操作账户期货可交易品种/合约配置的ag主力"""
        time.sleep(1)
        self.click(self.ag_element)
        return self

    def click_Commission_configuration(self):
        """选择配置"""
        self.click(self.configuration)
        return self

    def click_zaopan1(self):
        """点击早盘交易品种"""
        self.click(self.zaopan1_element)
        return self

    def click_yepan1(self):
        """点击夜盘交易品种"""
        self.click(self.yepan1_element)
        return self

    def input_net_worth(self):
        """输入净值"""
        self.find_element(self.net_worth).send_keys('8')
        return self

    def click_select(self):
        """点击风控方案框"""
        self.click(self.btn_select1)
        return self

    def select_yujingxian(self):
        """点击预警线"""
        self.click(self.yujingxian)
        return self

    def zengjiaqujian(self):
        """点击增加区间"""
        self.click(self.zengjiaqujian_element)
        return self

    def click_peizhi(self, product):
        """点击配置"""
        peizhi_element = (
        'xpath', "//td[contains(text(),'{}')]//following-sibling::td//following-sibling::td//following-sibling::td".format(product))
        self.click(peizhi_element)
        return self

    def DailyCheckReport(self):
        """点击编辑产品"""
        self.click(self.DailyCheckReport_element)
        return self

    def newly(self):
        """点击新增"""
        self.click(self.newly_element)
        time.sleep(1)
        return self

    def fkfacp1(self):
        "点击风控方案配置"
        self.click(self.fkfacp1_element)
        return self

    def synonymname(self):
        """输入产品别名"""
        self.Situation_box(self.synonymname_element)
        self.find_element(self.synonymname_element).send_keys('测试的产品别名')
        return self

    def oldrealaccountNum(self):
        """输入最大绑定可绑定资金账户数量"""
        self.Situation_box(self.oldrealaccountNum_element)
        self.find_element(self.oldrealaccountNum_element).send_keys('9000')
        return self

    def accountNum(self):
        """输入最大可绑定操作账户数量"""
        self.Situation_box(self.accountNum_element)
        self.find_element(self.accountNum_element).send_keys('9000')
        return self

    def click_wancheng(self):
        """点击完成按钮"""
        self.click(self.wancheng)
        time.sleep(1)
        return self

    def get_actual(self):
        """获取实际结果"""
        el = self.find_element(self.actual_result).text
        return el

    def RiskPlanName(self):
        """输入风控方案名称"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        self.find_element(self.RiskPlanName_element).send_keys('测试风控名称')
        return self

    def click_quanxuan(self):
        """点击全选按钮"""
        time.sleep(1)
        self.driver.switch_to.parent_frame()
        self.click(self.quanxuan_element)
        return self

    def click_quanxuan3(self):
        """点击全选按钮"""
        time.sleep(1)
        self.click(self.quanxuan_element)
        return self

    def positionschecks(self):
        """批量删除"""
        self.click(self.positionschecks_element)
        return self

    def window_affirm2(self):
        """确认按钮用于第一个确认无法定位到的时候"""
        self.click(self.queren2)
        return self

    def fkqjcp1(self):
        """点击风控区间配置"""
        self.click(self.fkqjcp1_element)
        return self

    # def variety_select(self):
    #     """期货品种默认保证金率配置，选择品种"""
    #     time.sleep(1)
    #     js = "document.getElementsByName(\"dayarea_1\")[0].style.display='block'"
    #     self.driver.execute_script(js)
    #     variety_select_element = ('xpath', "//select[@name='dayarea_1']")
    #     select_elem = self.find_element(variety_select_element)
    #     select = Select(select_elem)
    #     select.select_by_value('-2')
    #     time.sleep(1)
    #     return self

    def get_actual_result(self):
        """获取到实际结果"""
        actual_element = ('xpath',"//td[@class='table_content_center']//following-sibling::td")
        el = self.find_element(actual_element).text

        actual_element2 = ('xpath', "//td[@class='table_content_center']//following-sibling::td//following-sibling::td")
        el1 = self.find_element(actual_element2).text
        return {'品种代码': el, '合约': el1}

    def get_actual2(self, cp):
        """获取平今转开仓合约配置得结果"""
        element = ('xpath', "//b[text()='产品[{}]平今转开仓合约配置']".format(cp))
        el = self.find_element(element).text
        return el

    def get_actual3(self):
        """获取平今转开仓合约配置得结果"""
        element = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")
        el = self.find_element(element).text
        return el

    def get_actual4(self):
        """获取平今转开仓合约配置得结果"""
        element = ('xpath', "//div[@move='ok']")
        el = self.find_element(element).text
        return el

    def select_account(self, account):
        """产品外部报单配置添加账号"""
        account_element = ('xpath', "//span[text()='{}']//preceding-sibling::img".format(account))
        self.click(account_element)
        return self

    def get_actual5(self):
        """获取外部报单配置的实际结果"""
        element = ('xpath', "//td[@class='table_content_center']//following-sibling::td")
        el = self.find_element(element).text

        element2 = ('xpath', "//td[@class='table_content_center']//following-sibling::td//following-sibling::td")
        el2 = self.find_element(element2).text
        return {'操作账户':el, '品种':el2}

    def pinzhongTBJY_quanxuan(self):
        """点击全选按钮"""
        quanxuanF = ('xpath', "//img[@class='quanxuanF']")
        self.click(quanxuanF)
        return self

    def variety_select(self):
        """品种交易模式，选择品种"""
        js = "document.getElementById(\"grouptradecontrol.productid\").style.display='block'"
        self.driver.execute_script(js)
        select_elem = self.find_element(self.variety_select_element)
        select = Select(select_elem)
        select.select_by_value('IF')
        time.sleep(1)
        return self

    def get_actual6(self):
        """获取品种交易模式的实际结果"""
        element = ('xpath', "//td[@class='table_content_center']")
        el = self.find_element(element).text

        element2 = ('xpath', "//td[@class='table_content_center']//following-sibling::td")
        el2 = self.find_element(element2).text
        return {'品种':el, '交易模式':el2}

    def get_actual7(self):
        """获取产品总结报告的实际结果"""
        element = ('xpath', "//input[@id='groupid']//preceding-sibling::span")
        el = self.find_element(element).text
        return el

    def tradingday(self):
        """输入文件估值的日期"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        self.find_element(self.tradingday_element).send_keys('2021-03-16')
        return self