"""登录成功后的首页"""
import time
from common.seleniunm_packaging import BasePage
from middleware.heandler import Hadnler
from middleware.pages.addfundaccount import AddFundAccount
from middleware.pages.company_Increased import EconomicsIncreased
from middleware.pages.product import IncreaseProduct


class IndexPage(BasePage):
    """登录成功后的首页"""
    title = '管理平台-融航商品期权资管平台'
    URL = Hadnler.yaml['host'] + Hadnler.yaml['path']

    # 修改密码元素
    index_locator = ('xpath', "//a[@id='_updatePassword']")
    # 点击抢投标
    invest_bin_locator = ('xpath', "//a[@class='mainmenu menuselected']")
    # 系统配置元素
    # system_layout = ('xpath', "//img[@src='/2.0.60.234AMS4/images/icon7.png']")
    system_layout = ('xpath', "//b[text()='系统配置']")
    # 找到第一层iframe
    # iframe_elem = self.driver.find_element_by_tag_name('iframe')
    # 经济管理公司
    economic_administration = ('xpath', "//a[@id='_companymanager']")
    # 经济管理公司新增
    newly_increased = ('xpath', "//a[@id='xinzeng']")
    # 登录账户新增
    newly_account = ('xpath', "//span[text()='新增']")
    # 定位资金账户配置元素
    capital_allocation = ('xpath', "//b[text()='资金账户配置']")
    # 定位资金账户配置
    account_management = ('xpath', "//a[@id='_realaccountManager']")
    # 定位资金账户新增
    newcapitalaccount = ('xpath', "//span[@class='bar_button2']")
    # 定位到产品管理
    product_admin = ('xpath', "//a[text()='产品管理']")
    # 定位到产品管理新增
    product_newly = ('xpath', "//a[@id='newgroupbutton']")
    # 定位原有客户开户
    original_register = ('xpath', "//a[@id='openaccount1']")
    # 定位到一键开户
    one_key_register = ('xpath', "//a[@id='openaccount3']")
    # 定位到新增客户开户
    new_register = ('xpath', "//a[@id='openaccount2']")
    # 定位操作账户管理
    account_management_element = ('xpath', "//a[@id='accountMenu']")
    # 定位到风险控制配置
    risk_control = ('xpath', "//b[text()='风险控制配置']")
    # 定位风控账户管理
    pneumatic_admin = ('xpath', "//a[text()='风控账户管理']")
    # 定位全局风险度配置
    Risk_allocation = ('xpath', "//a[text()='全局风险度配置']")
    # 定位到新增按钮（新增风控账户）
    new_pneumatic = ('xpath', "//a[@id='addA']")
    # 定位到品种合约配置
    variety_contract_allocation = ('xpath', "//b[text()='品种合约配置']")
    # 定位到全局不可交易品种/合约
    Not_trading = ('xpath', "//a[text()='全局不可交易品种/合约']")
    # 定位到模板配置
    template_element = ('xpath', "//b[text()='模板配置']")
    # 定位到品种开仓权限模板
    variety_open_jurisdiction = ('xpath', "//a[text()='品种开仓权限模板']")
    # 定位到保证金率模板管理
    margin_rate_element = ('xpath', "//a[text()='保证金率模板管理']")
    # 定位审核出入金确认按钮
    money_affirm = ('xpath', "//a[@id='1_queren']")
    # 定位审核出入金确认按钮2
    money_affirm2 = ('xpath', "//a[@id='2_queren']")
    # 定位到审核出入金得确认按钮
    audit_queren = ('xpath', "//input[@id='popup_ok']")
    # 获取出入金审核成功得结果
    get_results = ('xpath', "//div[@id='popup_message']")
    # 报单查询
    ReportQuery_element = ('xpath', "//a[@id='_ReportQuery']")
    # 核算信息
    SettlementManager_element = ('xpath',"//a[@id='_SettlementManager']")
    # 账户历史
    AccountHistoryManager_element = ('xpath', "//a[@id='_AccountHistoryManager']")
    # 资金划拨
    cachiomenu_element = ('xpath', "//a[@id='cachiomenu']")
    # 手工行权
    execorderMenu_element = ('xpath', "//a[@id='execorderMenu']")
    # 搜索输入框
    Search_input_box = ('xpath', "//input[@class='sousuo_button ac_input']")
    # 客户管理
    opencustomerlist_element = ('xpath', "//a[@id='opencustomerlist']")
    # 客户管理
    powermanagerlist_element = ('xpath', "//a[@id='powermanagerlist']")
    # 手续费上限
    rnustate_element = ('xpath', "//a[text()='手续费上限']")
    # 银行管理
    banking_managemen_element = ('xpath', "//a[text()='银行管理']")
    # 其它配置
    qitapeizi_element = ('xpath', "//b[text()='其他配置']")
    # 终端认证
    AuthInfoDispose_element = ('xpath', "//a[text()='终端认证配置']")
    # 交割月最小下单手数
    prodelimonthminmul_element = ('xpath', "//a[text()='交割月最小下单手数']")

    def click_prodelimonthminmul(self):
        """点击交割月最小下单手数"""
        time.sleep(1)
        from middleware.pages.theminimumorderpage import TheMinimumOrder
        self.click(self.prodelimonthminmul_element)
        return TheMinimumOrder(self.driver)

    def click_AuthInfoDispose(self):
        """点击终端认证配置"""
        time.sleep(1)
        from middleware.pages.AuthInfoDisposepage import AuthInfoDispose
        self.click(self.AuthInfoDispose_element)
        return AuthInfoDispose(self.driver)

    def click_qitapeizi(self):
        """点击其它配置"""
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(1)
        self.click(self.qitapeizi_element)
        return self

    def click_banking_managemen(self):
        """点击银行管理"""
        time.sleep(1)
        from middleware.pages.banking_managemenpage import BankingManagemen
        self.click(self.banking_managemen_element)
        return BankingManagemen(self.driver)

    def click_rnustate(self):
        """点击手续费上限"""
        time.sleep(1)
        from middleware.pages.servicechargepage import ServiceCharge
        self.click(self.rnustate_element)
        return ServiceCharge(self.driver)

    def click_powermanagerlist(self):
        """点击权限管理"""
        time.sleep(1)
        from middleware.pages.rightsmanagementpage import RightsManagement
        self.click(self.powermanagerlist_element)
        return RightsManagement(self.driver)

    def click_opencustomerlist(self):
        """点击客户管理"""
        time.sleep(1)
        from middleware.pages.customer_managementpage import CustomerManagement
        self.click(self.opencustomerlist_element)
        return CustomerManagement(self.driver)

    def result(self):
        """获取审核成功得结果"""
        time.sleep(1)
        el = self.find_element(self.get_results).text
        return el

    def click_audit_queren(self):
        """点击出入金得确认按钮"""
        time.sleep(1)
        self.click(self.audit_queren)
        return self

    def click_money_affirm(self):
        """点击审核出入金得确认按钮"""
        self.click(self.money_affirm)
        return self

    def click_money_affirm2(self):
        """点击审核出入金得确认按钮"""
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.money_affirm2)
        return self

    def get(self):
        self.driver.get(self.URL)
        time.sleep(1)
        return self

    def get_account_name(self):
        """获取修改密码"""
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@name='right']")
        self.driver.switch_to.frame(iframe_elem2)
        el = self.find_element(self.index_locator).text
        return el

    def click_invest_bin(self):
        # 点击抢投标按钮
        self.driver.find_element(*self.invest_bin_locator).click()
        return self

    def click_system_configuration(self):
        """点击系统配置"""
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        # self.driver.switch_to.frame(iframe_elem)
        # iframe_elem2 = self.driver.find_element_by_xpath("//frame[@src='/2.0.60.234AMS4/user_GetPower.action?request_locale=zh_US']")
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        # self.find_element(self.system_layout).click()
        time.sleep(1)
        self.click(self.system_layout)
        return self

    def click_economic_administration(self):
        """点击经济管理公司"""
        time.sleep(1)
        self.wait_element_visible(self.economic_administration).click()
        return self

    def economics_newly(self):
        """点击新增（经纪公司）"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        s = self.find_element(self.newly_increased)
        s.click()
        return EconomicsIncreased(self.driver)

    def login_account_newly(self):
        """点击新增（登录账户）"""
        from middleware.pages.NewAdministratorpage import NewAdministrator
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        s = self.find_element(self.newly_account)
        s.click()
        return NewAdministrator(self.driver)

    def click_capital_account_allocation(self):
        """点击资金账户配置"""
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(1)
        self.click(self.capital_allocation)
        return self

    def click_account_management(self):
        """点击资金账户管理"""
        self.wait_element_visible(self.account_management).click()
        return self

    def new_capital_account(self):
        """点击新增（资金账号）"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.newcapitalaccount)
        return AddFundAccount(self.driver)

    def click_product_admin(self):
        """点击资金账户配置下的产品管理"""
        time.sleep(1)
        self.click(self.product_admin)
        return self

    def click_product_admin2(self):
        """点击资金账户配置下的产品管理"""
        from middleware.pages.Productpage import GroupMenu
        time.sleep(1)
        self.click(self.product_admin)
        return GroupMenu(self.driver)

    def click_new_product(self):
        """点击新增（增加产品）"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.product_newly)
        return IncreaseProduct(self.driver)

    def click_existing_client(self):
        """点击原有客户开户"""
        from middleware.pages.accountopening import AccountOpening
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.original_register)
        return AccountOpening(self.driver)

    def click_ReportQuery(self):
        """点击报单查询"""
        from middleware.pages.ReportQuerypage import ReportQuery
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_left']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.ReportQuery_element)
        return ReportQuery(self.driver)

    def click__SettlementManager(self):
        """点击核算信息"""
        from middleware.pages.SettlementManagerpage import SettlementManager
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_left']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.SettlementManager_element)
        return SettlementManager(self.driver)

    def click_AccountHistoryManager(self):
        """点击账户历史"""
        from middleware.pages.AccountHistoryManagerpage import AccountHistoryManager
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_left']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.AccountHistoryManager_element)
        return AccountHistoryManager(self.driver)

    def click_cachiomenu(self):
        """点击资金划拨"""
        from middleware.pages.cachiomenupage import CacHiomenu
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_left']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.cachiomenu_element)
        return CacHiomenu(self.driver)

    def click_ExecorderMenu(self):
        """点击手工行权"""
        from middleware.pages.execorderMenupage import ExecorderMenu
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_left']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.execorderMenu_element)
        return ExecorderMenu(self.driver)

    def click_key_toregister_client(self):
        """点击一键开户"""
        from middleware.pages.accountopening import AccountOpening
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.one_key_register)
        time.sleep(1)
        return AccountOpening(self.driver)

    def operating_account_management(self):
        """点击操作账户管理"""
        from middleware.pages.accountmanagement import AccountManagement
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(3)
        self.click(self.account_management_element)
        return AccountManagement(self.driver)

    def operating_account_management2(self):
        """点击操作账户管理"""
        from middleware.pages.accountmanagement import AccountManagement
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(3)
        self.click(self.account_management_element)
        return AccountManagement(self.driver)

    def operating_account_management3(self):
        """点击操作账户管理"""
        from middleware.pages.accountmanagement import AccountManagement
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(2)
        self.click(self.account_management_element)
        return AccountManagement(self.driver)

    def click_new_account(self):
        """点击新增客户开户"""
        from middleware.pages.newclientregister import NewClientRegister
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.new_register)
        return NewClientRegister(self.driver)

    def click_risk_control_allocation(self):
        """点击风险控制配置"""
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(1)
        self.click(self.risk_control)
        return self

    def click_pneumatic_admin(self):
        """点击风控账户管理"""
        self.wait_element_visible(self.pneumatic_admin).click()
        return self

    def click_Office_risk_allocation(self):
        """点击全局风险度配置"""
        from middleware.pages.globalriskallocationpage import GlobalRiskAllocation
        self.wait_element_visible(self.Risk_allocation).click()
        return GlobalRiskAllocation(self.driver)

    def click_new_risk(self):
        """点击新增（增加风控账号）"""
        from middleware.pages.addriskcontrolaccount import AddRiskControlAccountPage
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        time.sleep(1)
        self.click(self.new_pneumatic)
        return AddRiskControlAccountPage(self.driver)

    def click_Office_risk_allocation2(self):
        """点击全局风险度配置"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        from middleware.pages.globalriskallocationpage import GlobalRiskAllocation
        self.wait_element_visible(self.Risk_allocation).click()
        return GlobalRiskAllocation(self.driver)

    def click_Variety_contract_allocation(self):
        """点击品种合约配置"""
        from middleware.pages.tradableconfigpage import TradableConfig
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(1)
        self.click(self.variety_contract_allocation)
        time.sleep(1)
        return TradableConfig(self.driver)

    def click_Variety_contract_allocation2(self):
        """点击品种合约配置(返回的是对象)"""
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(1)
        self.click(self.variety_contract_allocation)
        time.sleep(1)
        return self

    def click_Not_trading(self):
        """点击全局不可交易品种/合约"""
        from middleware.pages.tradableconfigpage import TradableConfig
        self.wait_element_visible(self.Not_trading).click()
        return TradableConfig(self.driver)

    def click_template(self):
        """点击模板配置"""
        from middleware.pages.openthetemplate import OpenWarehousePermissionTemplate
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(1)
        self.click(self.template_element)
        return OpenWarehousePermissionTemplate(self.driver)

    def click_template1(self):
        """点击模板配置"""
        from middleware.pages.accountopening import AccountOpening
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(1)
        self.click(self.template_element)
        return AccountOpening(self.driver)

    def click_template2(self):
        """点击模板配置"""
        from middleware.pages.openthetemplate import OpenWarehousePermissionTemplate
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id ='upper_left']")
        self.switch_iframe(iframe_elem2)
        time.sleep(1)
        self.click(self.template_element)
        return self

    def click_variety_open_jurisdiction(self):
        """点击品种开仓权限模板"""
        from middleware.pages.openthetemplate import OpenWarehousePermissionTemplate
        self.click(self.variety_open_jurisdiction)
        return OpenWarehousePermissionTemplate(self.driver)

    def click_margin_rate(self):
        """点击保证金率模板管理"""
        from middleware.pages.MarginRateTemplatepage import MarginRateTemplate
        self.click(self.margin_rate_element)
        return MarginRateTemplate(self.driver)

    def input_product(self, account):
        """搜索框输入产品"""
        time.sleep(1)
        self.find_element(self.Search_input_box).send_keys(account)
        return self