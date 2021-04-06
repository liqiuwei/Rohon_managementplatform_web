import time

from selenium.webdriver.support.select import Select
from middleware.heandler import Hadnler
from common.seleniunm_packaging import BasePage
from middleware.pages.homepage import IndexPage


class AccountOpening(BasePage):
    """原有账户开/一键开户首页"""
    title = '管理平台-融航商品期权资管平台'
    # 定位开户人姓名输入框
    account_name = ('xpath', "//input[@id='customeName']")
    # 一键开户的开户人姓名
    account_name2 = ('xpath', "//input[@id='CustomeId']")
    # 定位账号登录输入框
    to_login = ('xpath', "//input[@id='LoginAccount']")
    # 定位到密码输入框
    enter_pwd = ('xpath', "//input[@id='PasswordCheck']")
    # 定位到下一步按钮
    next_step = ('xpath', "//input[@id='next']")
    # 定位获取结果元素
    actual_result = ('xpath', "//div//div[@id='popup_message']")
    # 获取到该操作账户已存在的元素
    actual_result2 = ('xpath',
                      "//div//div[@style='background-color:#fafafa;height:70px;text-align:left;padding-left:150px;padding-right:50px;vertical-align: middle;']")
    # 定位到窗口的确认按钮
    queren = ('xpath', "//input[@id='popup_close']")
    # 定位到窗口的确认按钮
    queren2 = ('xpath', "//input[@id='popup_ok']")
    # 定位到开户成功后的文本
    successful_outcome = ('xpath', "//b[contains(text(),'期货品种保证金')]")
    # 定位到品种保证金的新增元素
    variety_deposit = ('xpath', "//span[text()='新增']")
    # 定位到品种保证金的新增元素
    variety_deposit2 = ('xpath', "//span[text()='新建']")
    # 定位到品种id选择框
    variety_select_element = ('xpath', "//select[@id='ProductID']")
    # 定位到选按手数保证金费率输入框
    number_earnest_element = ('xpath', "//input[@id='LMarginRateByVol']")
    # 定位到按金额保证金率输入框
    money_margin_rate = ('xpath', "//input[@id='LMarginRateByMoney']")
    # 定位到期货品种默认保证金率配置的确认按钮
    queding = ('xpath', "//input[@id='queding']")
    # 定位到合约id输入框
    contract = ('xpath', "//input[@id='ProductID']")
    # 定位到预期结果期货合约保证金
    successful_contract_outcome = ('xpath', "//b[contains(text(),'期货合约保证金')]")
    # 定位按手数手续费率输入框
    shoushu_service = ('xpath', "//input[@id='OpenCommissionRateByVol']")
    # 定位按金额手续费率输入框
    money_service = ('xpath', "//input[@id='OpenCommissionRateByMoney']")
    # 定位到品种手续费文本
    variety_service_text = ('xpath', "//b[contains(text(),'品种手续费')]")
    # 定位到期货合约手续费文本
    commission_contracts = ('xpath', "//b[contains(text(),'期货合约手续费')]")
    # 定位到限制品种
    limited_varieties = ('xpath', "//span[text()='限制品种']")
    # 定位到限制品种
    astrict_element = ('xpath', "//span[text()='限制合约']")
    # 定位持仓量上限
    rosition_ceiling = ('xpath', "//input[@id='positions']")
    # 定位持仓保证金上限
    Margin_ceiling = ('xpath', "//input[@id='positionsamount']")
    # 定位期货品种限制的文本
    position_limits = ('xpath', "//b[contains(text(),'期货品种持仓限制')]")
    # 定位到配置按钮
    configuration = ('xpath', "//span[text()='配置']")
    # 定位到品种
    variety_element = ('xpath', "//img[@id='product_cu']")
    # 定位合约
    contract_element = ('xpath', "//img[@myvalue='ag主力']")
    # 定位到可交易品种/合约配置的确定按钮
    queding2 = ('xpath', "//input[@id='queding' and @class='addSub']")
    # 定位到可交易品种/合约文本
    variety_contract_text = ('xpath',
                             "//div[@style='font-size:20px;width: 90%;height: 30px;margin: 27px auto 0px;font-weight: bold;color: #67717e;']")
    # 定位到李秋维的产品
    select_product_element = ('xpath', "//img[@id='chanpinming1']")
    # 定位到选择一个风控账户
    pneumatic_account_element = ('xpath', "//img[@myvalue='monitor']")
    # 定位到转入转出输入框
    roll_inroll_out = ('xpath', "//input[@id='MONEY']")
    # 定位到备注输入框
    remark_element = ('xpath', "//input[@id='Comments']")
    # 获取到添加待审核出入金成功！
    gei_assert_element = ('xpath', "//div[@id='popup_message']")
    # 定位完成按钮
    wancheng = ('xpath', "//input[@id='queding']")
    # 定位一键开户的证件号码
    Number_element = ('xpath', "//input[@id='rohon_cus_idcard']")
    # 定位到选择保证金模板
    Margin_template = ('xpath', "//img[@class='margin']")
    # 选择手续费模板
    Commission_template = ('xpath', "//img[@class='commission']")
    # 配置可交易不可交易模板
    template_element = ('xpath', "//img[@class='instrument']")
    # 定位到品种停板交易权限模板配置
    trading_halt = ('xpath', "//img[@class='productlimit']")
    # 选择产品
    product_element = ('xpath', "//img[@id='李秋维的产品']")
    # 选择风控账户
    risk_management = ('xpath', "//img[@myvalue ='monitor']")
    # 保证金配置
    Margin_allocation = ('xpath', "//img[@class='round' and @myvalue='1']")
    # 手续费配置
    configuration1 = ('xpath', "//img[@class='circle' and @myvalue='1']")
    # 持仓量上限
    TotalPositions_element = ('xpath', "//input[@id='TotalPositions']")
    # 持仓保证金上限
    totalPosCost = ('xpath', "//input[@id='TotalPosCost']")
    # 合约最大撤单次数
    MaximumWithdrawals_element = ('xpath', "//input[@id='MaximumWithdrawals']")
    # 隔夜最大保证金风险度
    OvernightMaginRiskRate_element = ('xpath', "//input[@id='OvernightMaginRiskRate']")
    # 点击隔夜最大保证金风险度的高级
    gaoji_elenmet = ('xpath', "//a[@name='gaoji']")
    # 隔夜保证金风险控制方式为劣后资金
    After_money_element = ('xpath', "//img[@class='circle2' and @myvalue='2']")
    # 隔夜减仓方式为绝对敞口市值
    Cut_way_element = ('xpath', "//img[@class='circle5' and @myvalue='2']")
    # 隔夜绝对敞口市值超限时为禁开
    OVERNIGHTMARCLOSETYPE_element = ('xpath', "//img[@class='roundimg' and @myvalue='2']")
    # 追保风险度
    AppendMarginRate_element = ('xpath', "//input[@id='AppendMarginRate']")
    # 设置强平风险度
    ForceClose_element = ('xpath', "//input[@id='ForceClose']")
    # 当日亏损追保线
    DayMaxLossNotice_element = ('xpath', "//input[@id='DayMaxLossNotice']")
    # 当日亏损强平线
    DayMaxLossForce_element = ('xpath', "//input[@id='DayMaxLossForce']")
    # 最大日亏损追保比例
    DayMaxLossNoticeRate_element = ('xpath', "//input[@id='DayMaxLossNoticeRate']")
    # 最大日亏损强平比例：
    DayMaxLossForceRate_element = ('xpath', "//input[@id='DayMaxLossForceRate']")
    # 最大日亏损追保比例的高级
    gaoji2_elenmet = ('xpath', "//a[text()='高级']")
    # 最大日亏损风险控制方式为期初资金
    Maximum_element = ('xpath', "//img[@class='circle3' and @myvalue='3']")
    # 总亏损追保比例
    SummaryLossNoticeRatio_element = ('xpath', "//input[@id='SummaryLossNoticeRatio']")
    # 总亏损强平比例
    SummaryLossForceRatio_element = ('xpath', "//input[@id='SummaryLossForceRatio']")
    # 总亏损追保比例的高级
    gaoji3_elenmet = ('xpath', "//a[text()='高级']")
    # 总亏损风险控制方式为劣后总资金
    Total_element = ('xpath', "//img[@class='radio0' and @myvalue='2']")
    # 持仓保证金比例
    MarginRatio_element = ('xpath', "//input[@id='MarginRatio']")
    # 总亏损追保比例的高级
    gaoji4_elenmet = ('xpath', "//a[text()='高级']")
    # 持仓保证金风险控制方式
    Risk_mode_element = ('xpath', "//img[@class='circle4' and @myvalue='2']")
    # 保证金配置为跟随资金账户
    Margin_allocation_element = ('xpath', "//img[@class='round' and @myvalue='2']")
    # 手续费配置为跟随资金账户
    Commission_configuration_element = ('xpath', "//img[@class='circle' and @myvalue='2']")
    # 收取申报费用为不收取
    Collection_declaration_element = ('xpath', "//img[@class='circle1' and @myvalue='0']")
    # 平仓忽略敞口
    Close_exposures_element = ('xpath', "//img[@class='closecircle' and @myvalue='1']")
    # 份额设置
    realcapitalamount_element = ('xpath', "//input[@id='realcapitalamount']")
    # 历史最大权益
    historymaxprofit_element = ('xpath', "//input[@id='historymaxprofit']")
    # 允许交易套保单
    Allow_policies_element = ('xpath', "//img[@class='square8' and @myvalue='1']")
    # 收盘计算隔夜风险
    square_beforenight_element = ('xpath', "//img[@class='square_beforenight' and @myvalue='1']")
    # 是否支持大商所套保套利认定
    square_dcesupporthedging_lemenet = ('xpath', "//img[@class='square_dcesupporthedging' and @myvalue='1']")
    # 点击选择出入金转出转入
    churujinxuanze_element = ('xpath', "//div[@class='btn-select']")
    # 点击出入金转出
    zhuanchu_element = ("xpath", "//li[@id='zhuanchu']")
    # 获取到转入的出入金额(劣后资金)
    zhuanru_jine_element = (
        'xpath', "//td[@id='Direction1']//following-sibling::td//following-sibling::td[@class='table_content_center']")
    # 获取到转入的出入金额(优先资金)
    zhuanru_jine_element2 = (
        'xpath',
        "//td[@id='Direction1']//following-sibling::td//following-sibling::td//following-sibling::td[@class='table_content_center']")
    # 点击出入金转出转入的高级
    churujin_gaoji = ('xpath', "//span[@id='gaoji']")
    # 定位出入金的优先资金输入框
    CREDIT_element = ('xpath', "//input[@id='CREDIT']")
    # 定位到全选按钮
    quanxuan_element = ('xpath', "//img[@class='quanxuan']")
    # 定位到全选按钮
    quanxuan2_element = ('xpath', "//img[@id='facecheckboxtoselectall']")
    # 定位批量删除按钮
    plscaccountmargincode_element = ('xpath', "//span[@onclick='plscaccountmargincode()']")
    # 定位期货品种保证金批量删除按钮
    plscaccountmargincode_element2 = ('xpath', "//span[@onclick='plscaccountmarginproduct()']")
    # 定位到相对资金账户绝对值收取
    ChargeType_element = ('xpath', "//img[@id='_ChargeType']")
    # 相对资金账户百分比加收
    ChargeType3_element = ('xpath', "//img[@id='_ChargeType3']")
    # 期货合约手续费得批量删除
    plscaccountcommissioncode_element = ('xpath', "//span[@onclick='plscaccountcommissioncode()']")
    # 品种手续费的批量删除
    plscaccountcommissionproduct_element = ('xpath', "//span[@onclick='plscaccountcommissionproduct()']")
    # 期货品种持仓配置的批量删除
    positionschecks_element = ('xpath', "//span[text()='批量删除']")
    # 品种单边禁开配置的删除
    shanchu_element = ('xpath', "//a[contains(text(),'删除')]")
    # 新增品种单边禁开配置-定位到能源交易所
    exchange_INE_element = ('xpath', "//img[@id='exchange_INE']")
    # 定位到操作账户期货可交易品种/合约配置的ag
    ag_element = ('xpath', "//img[@id='product_ag']")
    # 定位到操作账户期货可交易品种/合约配置的ag的ag主力
    agzhuli_element = ('xpath', "//img[@id='product_ag']")
    # 定位到操作账户期货可交易品种/合约的全选按钮
    quanxuan3_element = ('xpath', "//img[@class='quanxuanF quanxuanC']")
    # 操作账户期货可交易品种/合约的删除
    shanchu2_element = ('xpath', "//span[text()='删除']")
    # 定位到期货品种开仓权限详细配置的上限输入框
    HighPrice_element = ('xpath', "//input[@id='HighPrice']")
    # 定位到期货品种开仓权限详细配置的下限输入框
    LowPrice_element = ('xpath', "//input[@id='LowPrice']")
    # 定位到绑定期货保证金率模板
    bangdingBZJ_element = ('xpath', "//a[@id='bangdingBZJ']")
    # 定位品种停板交易权限的一级风险输入框
    warnHighLimit_element = ('xpath', "//input[@id='warnHighLimit']")
    # 定位品种停板交易权限的二级风险输入框
    highlimit_element = ('xpath', "//input[@id='highlimit']")
    # 定位到删除按钮
    shanchu3_element = ('xpath', "//span[text()='删除']")
    # 定位到品种限制
    Varieties_limit_element = ('xpath', "//span[text()='品种限制']")
    # 定位到合约限制
    Contract_limit_element = ('xpath', "//span[text()='合约限制']")
    # 定位到期货品种单笔最大保证金/报单配置的最大保证金
    bjMaxCost_element = ('xpath', "//input[@id='bjMaxCost']")
    # 定位到期货品种单笔最大保证金/报单配置的报价限制比例
    pricepercent_element = ('xpath', "//input[@id='pricepercent']")
    # 定位到期货品种单笔最大保证金/报单配置的最大报单开仓数量
    bjMaxVol_element = ('xpath', "//input[@id='bjMaxVol']")
    # 定位到期货品种单笔最大保证金/报单配置的最大报单平仓数量
    bjCloseMaxVol_element = ('xpath', "//input[@id='bjCloseMaxVol']")
    # 定位到期货品种单笔最大保证金/报单配置的最小报单开仓数量
    OpenMinVol_element = ('xpath', "//input[@id='OpenMinVol']")
    # 定位到期货品种单笔最大保证金/报单配置的最小报单平仓数量
    CloseMinVol_element = ('xpath', "//input[@id='CloseMinVol']")
    # 定位到新增单一IP
    Added_Whitelist_element = ('xpath', "//span[text()='新增单一IP']")
    # 定位到新增单一IP
    Added_Whitelist_combination_element = ('xpath', "//span[text()='新增IP段']")
    # 定位到ip白名单输入框
    opipfilter_ipbegin_element = ('xpath', "//input[@id='opipfilter_ipbegin']")
    # 定位到ip白名单结尾输入框
    opipfilter_ipend_element = ('xpath', "//input[@id='opipfilter_ipend']")
    # 定位到MAC白名单绑定输入框
    opmacfilter_mac_element = ('xpath', "//input[@id='opmacfilter_mac']")
    # 定位到mac地址的新建
    xinjian_element = ('xpath', "//span[text()='新建']")
    # 定位到选择期权标的品种/合约的cf
    product_CF_element = ('xpath', "//img[@id='product_CF']")
    # 定位到标的品种或者标的合约选择框
    faceoppositionlimit_objCode = ('xpath', "//p[@id='faceoppositionlimit_objCode']")
    # 定位到多头限制得输入框
    duotouall_element = ('xpath', "//input[@id='duotouall']")
    # 定位到空头限制输入框
    kongtouall_element = ('xpath', "//input[@id='kongtouall']")
    # 定位到市价单每次最大下单手数输入框
    opordervolumelimit_maxmarketordervolume_element = ('xpath', "//input[@id='opordervolumelimit_maxmarketordervolume']")
    # 定位到	限价单每次最大下单手数
    opordervolumelimit_maxlimitordervolume_element = ('xpath', "//input[@id='opordervolumelimit_maxlimitordervolume']")
    # 期权下单量限制表管理-标的品种或者标的合约选择框
    btnselectopordervolumelimit_objcode_element = ('xpath', "//div[@id='btnselectopordervolumelimit_objcode']")
    # 权撤单限制 - 标的品种或者标的合约
    objcode6IO_element = ('xpath', "//li[text()='IO']")
    # 期权下单量限制表管理-标的品种或者标的合约选择框
    btnselectopcanclevolumelimit_objcode_element = ('xpath', "//div[@id='btnselectopcanclevolumelimit_objcode']")
    # 期权撤单限制-单日最大撤单笔数限制
    opcanclevolumelimit_maxcanclenumberlimitbyoneday_element = ('xpath', "//input[@id='opcanclevolumelimit_maxcanclenumberlimitbyoneday']")
    # 可交易不可交易模板
    ProductNotCantradeAndCantradeTemplate_element = ('xpath', "//a[@id='_ProductNotCantradeAndCantradeTemplate']")
    # 可交易不可交易模板配置模板名称
    rohon_acinte_name_element = ('xpath', "//input[@id='rohon_acinte_name']")
    # 报单限制模板新增
    rohon_acinte_name_element2 = ('xpath', "//input[@id='oporderrestricttemplate_name']")
    # 报单限制模板新增
    rohon_acinte_name_element3 = ('xpath', "//input[@id='oppositionstemplate_name']")
    # 报单限制模板新增
    rohon_acinte_name_element4 = ('xpath', "//input[@id='opproductlimittemplate_name']")
    # 搜索框
    researchString_element = ('xpath', "//input[@id='researchString']")
    # 搜索按钮
    shousuo_element  = ('xpath', "//img[@onclick='search()']")
    # 定位到操作里面的可交易按钮
    kejiaoyi = ('xpath', "//li//a[contains(text(),'可交易')]")
    # 定位到操作里面的不可交易按钮
    bukejiaoyi = ('xpath', "//li//a[contains(text(),'不可交易')]")
    # 定位到返回
    quxiao_element = ('xpath', "//input[@id='quxiao']")
    # 定位到操作里面的期权开仓限制按钮
    qiquankaichang_element = ('xpath', "//li//a[contains(text(),'期权开仓限制')]")
    # 输入模板名称
    name_element = ('xpath', "//input[@id='name']")
    # 手续费模板管理
    CommisionTempManager_element = ('xpath', "//a[@id='_CommisionTempManager']")
    # 手续费优惠规则模板
    commissionFavRuleTemplate_element = ('xpath', "//a[@id='_commissionFavRuleTemplate']")
    # 报单限制模板
    mainmenu_menuselected_element = ('xpath', "//a[text()='报单限制模板']")
    # 品种持仓配置模板
    Variety_position_allocation_element = ('xpath', "//a[text()='品种持仓配置模板']")
    # 品种停板交易权限模板
    Variety_suspended_trading_element = ('xpath', "//a[text()='品种停板交易权限模板']")

    def click_Variety_suspended_trading(self):
        """点击品种停板交易权限模板"""
        self.click(self.Variety_suspended_trading_element)
        return self

    def click_Variety_position_allocation(self):
        """点击品种持仓配置模板"""
        self.click(self.Variety_position_allocation_element)
        return self

    def click_mainmenu_menuselected(self):
        """点击手续费优惠规则模板"""
        self.click(self.mainmenu_menuselected_element)
        return self

    def click_commissionFavRuleTemplate(self):
        """点击手续费优惠规则模板"""
        self.click(self.commissionFavRuleTemplate_element)
        return self

    def click_CommisionTempManager(self):
        """点击手续费模板管理"""
        self.click(self.CommisionTempManager_element)
        return self

    def rohon_acinte_name2(self):
        """输入模板名称"""
        self.find_element(self.name_element).send_keys('测试模板名称')
        return self

    def click_qiquankaichang(self):
        """点击期权开仓限制"""
        self.click(self.qiquankaichang_element)
        return self

    def click_bukejiaoyi(self):
        """点击不可交易按钮"""
        self.click(self.bukejiaoyi)
        return self

    def click_quxiao(self):
        """点击返回按钮"""
        self.driver.switch_to.parent_frame()
        self.click(self.quxiao_element)
        return self

    def get_actual3(self):
        """获取到实际结果"""
        element = ('xpath', "//td[@class='table_content_center']//following-sibling::td")
        el = self.find_element(element).text

        element2 = ('xpath', "//td[@class='table_content_center']//following-sibling::td//following-sibling::td")
        el2 = self.find_element(element2).text
        return {'品种代码': el, "合约": el2}

    def click_kejiaoyi(self):
        """点击可交易按钮"""
        self.click(self.kejiaoyi)
        return self

    def click_operation(self, name='测试模板名称'):
        """点击操作按钮"""
        time.sleep(1)
        operation = ('xpath', "//td[contains(text(),'{}')]//following-sibling::td//following-sibling::td".format(name))
        self.click(operation)
        return self

    def researchString(self):
        """输入搜索内容点击搜索"""
        self.find_element(self.researchString_element).send_keys('测试模板名称')
        self.click(self.shousuo_element)
        return self

    def researchString2(self):
        """输入搜索内容点击搜索"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.find_element(self.researchString_element).send_keys('测试模板名称')
        self.click(self.shousuo_element)
        return self

    def researchString3(self):
        """输入搜索内容点击搜索"""
        self.find_element(self.researchString_element).send_keys('测试模板名称')
        self.click(self.shousuo_element)
        return self

    def researchString4(self):
        """输入搜索内容点击搜索"""
        self.driver.switch_to.parent_frame()
        self.find_element(self.researchString_element).send_keys('测试模板名称')
        self.click(self.shousuo_element)
        return self


    def rohon_acinte_name(self):
        """输入模板名称"""
        self.find_element(self.rohon_acinte_name_element).send_keys('测试模板名称')
        return self

    def rohon_acinte_name3(self):
        """输入模板名称"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        self.find_element(self.rohon_acinte_name_element3).send_keys('测试模板名称')
        return self

    def rohon_acinte_name5(self):
        """输入模板名称"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        self.find_element(self.rohon_acinte_name_element4).send_keys('测试模板名称')
        return self

    def rohon_acinte_name4(self):
        """输入模板名称"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        self.find_element(self.rohon_acinte_name_element2).send_keys('测试模板名称')
        return self

    def click_ProductNotCantradeAndCantradeTemplat(self):
        """点击可交易不可交易模板"""
        self.click(self.ProductNotCantradeAndCantradeTemplate_element)
        return self

    def click_quanxuan3(self):
        """点击操作账户期货可交易品种/合约的全选按钮"""
        self.click(self.quanxuan3_element)
        return self

    def shanchu2(self):
        """点击操作账户期货可交易品种/合约的删除"""
        self.click(self.shanchu2_element)
        return self

    def click_ag(self):
        """点击操作账户期货可交易品种/合约配置的ag主力"""
        time.sleep(1)
        self.click(self.agzhuli_element)
        return self

    def click_Margin_allocation(self):
        """选择自定义保证金配置"""
        self.click(self.Margin_allocation)
        return self

    def click_Commission_configuration(self):
        """选择自定义手续费配置"""
        self.click(self.configuration1)
        return self

    def select_risk_management(self, management):
        """选择风控账户"""
        # 选择风控账户
        risk_management = ('xpath', "//img[@myvalue ='{}']".format(management))
        self.click(risk_management)
        return self

    def select_product1(self, product1):
        """选择产品"""
        product_element = ('xpath', "//img[@id='{}']".format(product1))
        self.click(product_element)
        return self

    def click_trading_halt(self):
        """品种种停板交易权限模板配置"""
        self.click(self.trading_halt)
        return self

    def click_Margin_template(self):
        """选择保证金模板"""
        self.click(self.Margin_template)
        return self

    def click_Commission_template(self):
        """选择手续费模板"""
        self.click(self.Commission_template)
        return self

    def click_template(self):
        """配置可交易不可交易模板"""
        self.click(self.template_element)
        return self

    def input_number(self):
        """输入证件号码"""
        self.find_element(self.Number_element).send_keys('432702199505053196')
        return self

    def enter_the_name(self, name):
        """输入开户人姓名"""
        self.find_element(self.account_name).send_keys(name)
        return self

    def enter_the_name2(self, name):
        """一键开户的输入开户人姓名"""
        time.sleep(1)
        self.find_element(self.account_name2).send_keys(name)
        return self

    def enter_password(self, password):
        """输入密码"""
        self.find_element(self.enter_pwd).send_keys(password)
        return self

    def enter_password2(self):
        """输入密码"""
        self.find_element(self.enter_pwd).clear()
        return self

    def account_type(self, account):
        """输入登录账号"""
        self.find_element(self.to_login).send_keys(account)
        return self

    def get_actual(self):
        """获取实际结果"""
        el = self.find_element(self.actual_result).text
        return el

    def get_actual2(self):
        """获取该操作账户已存在的实际结果"""
        el = self.find_element(self.actual_result2).text
        return el

    def window_affirm(self):
        """点击窗口的确认按钮"""
        self.click(self.queren)
        return self

    def window_affirm2(self):
        """确认按钮用于第一个确认无法定位到的时候"""
        self.click(self.queren2)
        return self

    def window_affirm4(self):
        """确认按钮用于第一个确认无法定位到的时候"""
        time.sleep(1)
        self.click(self.queren2)
        return self

    def window_affirm3(self):
        """确认按钮用于第一个确认无法定位到的时候"""
        from middleware.pages.homepage import IndexPage
        time.sleep(1)
        self.click(self.queren2)
        return IndexPage(self.driver)

    def empty_message_input(self):
        """清空输入框"""
        self.find_element(self.account_name).clear()
        self.find_element(self.to_login).clear()
        self.find_element(self.enter_pwd).clear()
        return self

    def futures_margin(self):
        """开户成功后的实际结果文本"""
        time.sleep(2)
        el = self.find_element(self.successful_outcome).text
        return el

    def variety_earnest_newly(self):
        """点击品种保证金的新增按钮(后面新增通用)"""
        self.click(self.variety_deposit)
        time.sleep(1)
        return self

    def variety_earnest_newly2(self):
        """点击品种保证金的新增按钮(后面新增通用)"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.variety_deposit)
        time.sleep(1)
        return self

    def variety_earnest_newly3(self):
        """点击品种保证金的新增按钮(后面新增通用)"""
        self.driver.switch_to.parent_frame()
        iframe_elem2 = self.driver.find_element_by_xpath("//frame[@id='upper_right']")
        self.driver.switch_to.frame(iframe_elem2)
        self.click(self.variety_deposit2)
        time.sleep(1)
        return self

    def Limited_varieties(self):
        """点击限制品种按钮"""
        self.click(self.limited_varieties)
        time.sleep(1)
        return self

    def astrict(self):
        """点击限制品种按钮"""
        self.click(self.astrict_element)
        iframe_elem = self.driver.find_element_by_tag_name('iframe')
        self.switch_iframe(iframe_elem)
        return self

    def variety_select(self):
        """期货品种默认保证金率配置，选择品种"""
        js = "document.getElementById(\"ProductID\").style.display='block'"
        self.driver.execute_script(js)
        select_elem = self.find_element(self.variety_select_element)
        select = Select(select_elem)
        select.select_by_value('TCFFEX')
        time.sleep(1)
        return self

    def number_earnest(self, figure='100'):
        """输入按手数保证金费率"""
        self.Situation_box(self.number_earnest_element)
        self.find_element(self.number_earnest_element).send_keys(figure)
        return self

    def amount_margin_rate(self, figure='10'):
        """按金额保证金率"""
        self.Situation_box(self.money_margin_rate)
        self.find_element(self.money_margin_rate).send_keys(figure)
        return self

    def variety_configuration_queding(self):
        """点击期货品种默认保证金率配置(和下一步通用)"""
        time.sleep(1)
        self.click(self.queding)
        return self

    def variety_configuration_queding2(self):
        """点击期货品种默认保证金率配置(和下一步通用)"""
        self.click(self.queding)
        return self

    def import_contract(self):
        """输入合约id"""
        self.find_element(self.contract).send_keys(Hadnler.yaml['contract'])
        time.sleep(1)
        return self

    def import_contract2(self):
        """输入合约id"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        self.find_element(self.contract).send_keys(Hadnler.yaml['contract'])
        time.sleep(2)
        return self

    def futures_margin1(self):
        """期货合约保证的文本"""
        time.sleep(2)
        el = self.find_element(self.successful_contract_outcome).text
        return el

    def shoushu_shouxufei(self):
        """按手数手续费率 """
        self.Situation_box(self.shoushu_service)
        self.find_element(self.shoushu_service).send_keys('100')
        return self

    def jine_shouxufei(self):
        """按金额手续费率"""
        self.Situation_box(self.money_service)
        self.find_element(self.money_service).send_keys('10')
        return self

    def empty_message_input1(self):
        """清空品种默认手续费率配置输入框"""
        self.Situation_box(self.money_service)
        self.Situation_box(self.shoushu_service)

        return self

    def futures_margin2(self):
        """品种手续费的文本"""
        time.sleep(1)
        el = self.find_element(self.variety_service_text).text
        return el

    def commission_futures_Contracts(self):
        """定位到期货合约手续费的文本"""
        time.sleep(2)
        el = self.find_element(self.commission_contracts).text
        return el

    def variety_select2(self):
        """期货品种持仓限制配置，品种ID"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        js = "document.getElementById(\"ProductID\").style.display='block'"
        self.driver.execute_script(js)
        select_elem = self.find_element(self.variety_select_element)
        select = Select(select_elem)
        select.select_by_value('TCFFEX')
        time.sleep(1)
        return self

    def position_ceiling(self):
        """输入持仓量上限"""
        self.Situation_box(self.rosition_ceiling)
        self.find_element(self.rosition_ceiling).send_keys('100000')
        return self

    def Position_margin_limit(self):
        """输入持仓保证金上限"""
        self.Situation_box(self.Margin_ceiling)
        self.find_element(self.Margin_ceiling).send_keys('20,00000')
        return self

    def futures_position_limits(self):
        """期货品种持仓限制的文本"""
        self.driver.switch_to.parent_frame()
        time.sleep(1)
        el = self.find_element(self.position_limits).text
        return el

    def click_configuration(self):
        """点击配置按钮"""
        self.click(self.configuration)
        time.sleep(1)
        return self

    def select_variety(self):
        """选择品种"""
        time.sleep(1)
        self.click(self.variety_element)
        return self

    def select_contract(self):
        """选择合约"""
        time.sleep(1)
        self.click(self.contract_element)
        return self

    def click_queding(self):
        """可交易品种/合约配置的确定"""
        self.click(self.queding2)
        return self

    def get_variety_contract(self):
        """获取到可交易品种/合约文本"""
        time.sleep(1)
        el = self.find_element(self.variety_contract_text).text
        return el

    def judge_element(self):
        try:
            self.driver.find_element_by_xpath("//input[@id='customeName']")
            return True
        except Exception as err:
            return False

    def select_product(self, product):
        """选择产品"""
        # 定位到李秋维的产品
        select_product_element = ('xpath', "//input[@id='_bindgroup{}']//preceding-sibling::img".format(product))
        self.click(select_product_element)
        return self

    def select_pneumatic(self, pneumatic):
        """选择风控账户"""
        # 定位到选择一个风控账户
        pneumatic_account_element = ('xpath', "//img[@myvalue='{}']".format(pneumatic))
        time.sleep(1)
        self.click(pneumatic_account_element)
        return self

    def eliminate(self):
        """清除输入框的出入金"""
        self.Situation_box(self.roll_inroll_out)
        return self

    def eliminate2(self):
        """清除输入框的出入金"""
        self.Situation_box(self.roll_inroll_out)
        self.Situation_box(self.CREDIT_element)
        return self

    def eliminate3(self):
        """清除输入框的出入金"""
        self.Situation_box(self.roll_inroll_out)
        return self

    def transfer_amount(self, money='9000000'):
        """转入/转出输入框(劣后资金)"""
        self.find_element(self.roll_inroll_out).send_keys(money)
        return self

    def CREDIT_amount(self, money='1000000'):
        """转入/转出输入框(优先资金)"""
        self.find_element(self.CREDIT_element).send_keys(money)
        return self

    def remark_input_box(self, data='这是李秋维的测试开户备注，请勿动'):
        """出入金备注"""
        time.sleep(1)
        self.find_element(self.remark_element).send_keys(data)
        return self

    def get_gold(self):
        """获取到添加待审核出入金成功的文本"""
        el = self.find_element(self.gei_assert_element).text
        return el

    def click_wancheng(self):
        """点击完成按钮"""
        self.click(self.wancheng)
        time.sleep(1)
        return IndexPage(self.driver)

    def click_wancheng2(self):
        """点击完成按钮"""
        self.click(self.wancheng)
        return self

    def click_next(self):
        """点击下一步按钮"""
        time.sleep(1)
        self.click(self.next_step)
        time.sleep(1)
        return self

    def total_positions(self, number):
        """输入持仓量上限"""
        self.Situation_box(self.TotalPositions_element)
        self.find_element(self.TotalPositions_element).send_keys(number)
        return self

    def total_poscost(self, number):
        """输入持仓保证金上限"""
        self.Situation_box(self.totalPosCost)
        self.find_element(self.totalPosCost).send_keys(number)
        return self

    def MaximumWithdrawals(self, number):
        """最大撤单次数"""
        self.Situation_box(self.MaximumWithdrawals_element)
        self.find_element(self.MaximumWithdrawals_element).send_keys(number)
        return self

    def OvernightMaginRiskRate(self, number):
        """隔夜最大保证金风险度"""
        self.Situation_box(self.OvernightMaginRiskRate_element)
        self.find_element(self.OvernightMaginRiskRate_element).send_keys(number)
        return self

    def OvernightMaginRiskRate_gaoji(self):
        """点击隔夜最大保证金风险度的高级"""
        self.click(self.gaoji_elenmet)
        return self

    def click_After_money(self):
        """选择隔夜保证金风险控制方式为劣后资金"""
        # 数据库字段 OVERNIGHTMARDIVTYPE 2
        self.click(self.After_money_element)
        return self

    def clicl_Cut_way(self):
        """隔夜减仓方式为绝对敞口市值"""
        # 数据库字段 OVERNIGHTLIMITTYPE  2
        self.click(self.Cut_way_element)
        return self

    def OVERNIGHTMARCLOSETYPE(self):
        """隔夜绝对敞口市值超限时为禁开"""
        # 熟即可字段 OVERNIGHTMARCLOSETYPE 2
        self.click(self.OVERNIGHTMARCLOSETYPE_element)
        return self

    def AppendMarginRate(self, number):
        """设置追保风险度"""
        self.Situation_box(self.AppendMarginRate_element)
        self.find_element(self.AppendMarginRate_element).send_keys(number)
        return self

    def ForceClose(self, number):
        """设置强平风险度"""
        self.Situation_box(self.ForceClose_element)
        self.find_element(self.ForceClose_element).send_keys(number)
        return self

    def DayMaxLossNotice(self, number):
        """当日亏损追保线"""
        self.Situation_box(self.DayMaxLossNotice_element)
        self.find_element(self.DayMaxLossNotice_element).send_keys(number)
        return self

    def DayMaxLossForce(self, number):
        """当日亏损强平线"""
        self.Situation_box(self.DayMaxLossForce_element)
        self.find_element(self.DayMaxLossForce_element).send_keys(number)
        return self

    def DayMaxLossNoticeRate(self, number):
        """最大日亏损追保比例"""
        self.Situation_box(self.DayMaxLossNoticeRate_element)
        self.find_element(self.DayMaxLossNoticeRate_element).send_keys(number)
        return self

    def DayMaxLossForceRate(self, number):
        """最大日亏损强平比例"""
        self.Situation_box(self.DayMaxLossForceRate_element)
        self.find_element(self.DayMaxLossForceRate_element).send_keys(number)
        return self

    def Maximum(self):
        """最大日亏损风险控制方式的高级"""
        data = self.find_elements(self.gaoji2_elenmet)
        data[1].click()
        return self

    def Maximum_mode(self):
        """最大日亏损风险控制方式为期初资金"""
        # 数据库字段 DAYMAXLOSSDIVTYPE 3
        self.click(self.Maximum_element)
        return self

    def SummaryLossNoticeRatio(self, number):
        """总亏损追保比例"""
        self.Situation_box(self.SummaryLossNoticeRatio_element)
        self.find_element(self.SummaryLossNoticeRatio_element).send_keys(number)
        return self

    def SummaryLossForceRatio(self, number):
        """总亏损强平比例"""
        self.Situation_box(self.SummaryLossForceRatio_element)
        self.find_element(self.SummaryLossForceRatio_element).send_keys(number)
        return self

    def gaoji3(self):
        """总亏损追保比例的高级"""
        data = self.find_elements(self.gaoji3_elenmet)
        data[2].click()
        return self

    def Total(self):
        """总亏损风险控制方式为劣后总资金"""
        self.click(self.Total_element)
        return self

    def MarginRatio(self, number):
        """输入持仓保证金比例"""
        self.Situation_box(self.MarginRatio_element)
        self.find_element(self.MarginRatio_element).send_keys(number)
        return self

    def gaoji4(self):
        """总亏损追保比例的高级"""
        data = self.find_elements(self.gaoji4_elenmet)
        data[3].click()
        return self

    def Risk_mode(self):
        """持仓保证金风险控制方式为劣后资金"""
        # 数据库字段 MARGINRATIODIVTYPE 2
        self.click(self.Risk_mode_element)
        return self

    def Margin_allocation2(self):
        """保证金配置为跟随资金账户"""
        # 数据库字段为 MARGINSETTING  2
        self.click(self.Margin_allocation_element)
        return self

    def Commission_configuration(self):
        """手续费配置为跟随资金账户"""
        # 数据库字段为 COMMISSIONSETTING  2
        self.click(self.Commission_configuration_element)
        return self

    def Collection_declaration(self):
        """收取申报费为不收取"""
        # 数据库字段为 USEORDERFEE 0
        self.click(self.Collection_declaration_element)
        return self

    def Close_exposures(self):
        """平仓忽略敞口改为忽略"""
        # 数据库字段为 CLOSEIGNOREEXPOSURE 1
        self.click(self.Close_exposures_element)
        return self

    def realcapitalamount(self, number):
        """份额设置"""
        self.Situation_box(self.realcapitalamount_element)
        self.find_element(self.realcapitalamount_element).send_keys(number)
        return self

    def historymaxprofit(self, number):
        """历史最大权益"""
        self.Situation_box(self.historymaxprofit_element)
        self.find_element(self.historymaxprofit_element).send_keys(number)
        return self

    def Allow_policies(self):
        """允许交易套保单"""
        # 数据库的字段是 SUPPORTHEDGE 1
        self.click(self.Allow_policies_element)
        return self

    def square_beforenight(self):
        """收盘计算隔夜风险"""
        # 数据库的字段是 ISBEFORENIGHTCLOSED 1
        self.click(self.square_beforenight_element)
        return self

    def square_dcesupporthedging(self):
        """是否支持大商所套保套利认定"""
        # 数据库的字段是 DCESUPPORTHEDGING  1
        self.click(self.square_dcesupporthedging_lemenet)
        return self

    def get_attribute(self):
        """获取值的属性"""
        time.sleep(1)
        data = self.find_element(self.totalPosCost).get_attribute("value")
        print(data)
        return self

    def churujinxuanze(self):
        """点击出入金转出转入选择框"""
        self.click(self.churujinxuanze_element)
        return self

    def chujin_zhuanchu(self):
        """选择出入金为转出"""
        self.click(self.zhuanchu_element)
        return self

    def zhuanru_jine(self):
        """获取到转入金额(劣后资金)"""
        el = self.find_element(self.zhuanru_jine_element).text
        return el

    def churujingaoji(self):
        """点击出入金的高级"""
        self.click(self.churujin_gaoji)
        return self

    def zhuanru_jine2(self):
        """获取到转入金额(优先资金资金)"""
        el = self.find_element(self.zhuanru_jine_element2).text
        return el

    def click_quanxuan(self):
        """点击全选按钮"""
        self.click(self.quanxuan_element)
        return self

    def click_quanxuan2(self):
        """点击全选按钮"""
        time.sleep(1)
        self.click(self.quanxuan2_element)
        return self

    def click_plscaccountmargincode(self):
        """点击批量删除按钮"""
        self.click(self.plscaccountmargincode_element2)
        return self

    def click_plscaccountmargincode2(self):
        """点击批量删除按钮"""
        self.click(self.plscaccountmargincode_element)
        return self

    def get_Hand_more(self):
        """获取手数多的金额"""
        Handmore3 = ('xpath',
                     "//td[contains(text(),'{}')]".format(Hadnler.yaml['contract']))
        el3 = self.find_element(Handmore3).text
        Handmore4 = ('xpath',
                     "//td[contains(text(),'{}')]//following-sibling::td[@style='display:']".format(
                         Hadnler.yaml['contract']))
        el4 = self.find_element(Handmore4).text
        Handmore = ('xpath',
                    "//td[contains(text(),'{}')]//following-sibling::td[@class='table_content_center float right']".format(
                        Hadnler.yaml['contract']))
        el = self.find_element(Handmore).text
        Handmore = ('xpath',
                    "//td[contains(text(),'{}')]//following-sibling::td[@class='table_content_center floatpercent right']".format(
                        Hadnler.yaml['contract']))
        el2 = self.find_element(Handmore).text

        return {"手数多金额是": el, "金额多金额是": el2, "品种名称": el3, "收取方式": el4}

    def get_Hand_more2(self):
        """获取期货合约默认手续费率配置"""
        Handmore3 = ('xpath',
                     "//td[contains(text(),'{}')]".format(Hadnler.yaml['contract']))
        el3 = self.find_element(Handmore3).text

        Handmore4 = ('xpath',
                     "//td[contains(text(),'{}')]//following-sibling::td[@style='display:']".format(
                         Hadnler.yaml['contract']))
        el4 = self.find_element(Handmore4).text

        Handmore = ('xpath',
                    "//td[contains(text(),'{}')]//following-sibling::td[@class='table_content_center float right']".format(
                        Hadnler.yaml['contract']))
        el = self.find_element(Handmore).text

        Handmore2 = ('xpath',
                     "//td[contains(text(),'{}')]//following-sibling::td[@class='table_content_center floatpercent right']".format(
                         Hadnler.yaml['contract']))
        el2 = self.find_element(Handmore2).text

        return {"按手数开仓": el, "按金额开仓": el2, "品种名称": el3, "收取方式": el4}

    def get_Hand_mor2e(self):
        """获取手数多的金额"""
        Handmore3 = ('xpath',
                     "//td[contains(text(),'T')]")
        el3 = self.find_element(Handmore3).text

        Handmore = ('xpath',
                    "//td[contains(text(),'T')]//following-sibling::td[@class='table_content_center float right']")
        el = self.find_element(Handmore).text

        Handmore2 = ('xpath',
                     "//td[contains(text(),'T')]//following-sibling::td[@class='table_content_center floatpercent right']")
        el2 = self.find_element(Handmore2).text

        Handmore4 = ('xpath',
                     "//td[contains(text(),'T')]//following-sibling::td[@style='display:']")
        el4 = self.find_element(Handmore4).text

        return {"手数多金额是": el, "金额多金额是": el2, "品种名称": el3, "收取方式": el4}

    def get_Hand_mor2(self):
        """获取手数多的金额"""
        Handmore3 = ('xpath',
                     "//td[contains(text(),'T')]")
        el3 = self.find_element(Handmore3).text

        Handmore = ('xpath',
                    "//td[contains(text(),'T')]//following-sibling::td[@class='table_content_center float right']")
        el = self.find_element(Handmore).text

        Handmore2 = ('xpath',
                     "//td[contains(text(),'T')]//following-sibling::td[@class='table_content_center floatpercent right']")
        el2 = self.find_element(Handmore2).text

        Handmore4 = ('xpath',
                     "//td[contains(text(),'T')]//following-sibling::td[@style='display:']")
        el4 = self.find_element(Handmore4).text

        return {"按手数开仓": el, "按金额开仓": el2, "品种名称": el3, "收取方式": el4}

    def get_productpositions_result(self):
        """期货品种持仓限制配置的结果"""
        self.driver.switch_to.parent_frame()
        Handmore3 = ('xpath', "//td[contains(text(),'T')]")
        el3 = self.find_element(Handmore3).text

        Handmore = ('xpath',
                    "//td[contains(text(),'T')]//following-sibling::td[@class='table_content_center right']")
        el = self.find_element(Handmore).text

        Handmore2 = ('xpath',
                     "//td[contains(text(),'T')]//following-sibling::td//following-sibling::td[@class='table_content_center right']")
        el2 = self.find_element(Handmore2).text

        Handmore4 = ('xpath',
                     "//td[contains(text(),'T')]//following-sibling::td[@class='table_content_center']")
        el4 = self.find_element(Handmore4).text

        return {"持仓量上限": el, "持仓保证金上限": el2, "品种名称": el3, "持仓类型": el4}

    def get_productpositions_result2(self):
        """期货合约持仓限制配置的结果"""
        self.driver.switch_to.parent_frame()
        Handmore3 = ('xpath', "//td[contains(text(),'{}')]".format(Hadnler.yaml['contract']))
        el3 = self.find_element(Handmore3).text

        Handmore = ('xpath',
                    "//td[contains(text(),'{}')]//following-sibling::td[@class='table_content_center right']".format(
                        Hadnler.yaml['contract']))
        el = self.find_element(Handmore).text

        Handmore2 = ('xpath',
                     "//td[contains(text(),'{}')]//following-sibling::td//following-sibling::td[@class='table_content_center right']".format(
                         Hadnler.yaml['contract']))
        el2 = self.find_element(Handmore2).text

        Handmore4 = ('xpath',
                     "//td[contains(text(),'{}')]//following-sibling::td[@class='table_content_center']".format(
                         Hadnler.yaml['contract']))
        el4 = self.find_element(Handmore4).text

        return {"持仓量上限": el, "持仓保证金上限": el2, "品种名称": el3, "持仓类型": el4}

    def ChargeType(self):
        """点击相对资金账户绝对值收取"""
        self.click(self.ChargeType_element)
        return self

    def ChargeType3(self):
        """点击相对资金账户绝对值收取"""
        self.click(self.ChargeType3_element)
        return self

    def isPresent2(self, contract):
        """判断元素是否存在"""
        Xpath = "//td[contains(text(),'{}')]".format(contract)
        try:
            self.driver.find_element_by_xpath(Xpath)
        except Exception as err:
            return False
        return True

    def plscaccountcommissioncode(self):
        """点击期货合约手续费得批量删除"""
        self.click(self.plscaccountcommissioncode_element)
        return self

    def plscaccountcommissionproduct(self):
        """品种手续费的删除"""
        self.click(self.plscaccountcommissionproduct_element)
        return self

    def positionschecks(self):
        """期货品种持仓配置的删除"""
        self.click(self.positionschecks_element)
        return self

    def exchange_INE(self):
        """点击新增品种单边禁开配置的能源中心"""
        self.click(self.exchange_INE_element)
        return self

    def get_result(self):
        """获取品种单边禁开配置的结果"""
        Handmore = ('xpath',
                    "//td[contains(text(),'禁买开')]")
        el = self.find_element(Handmore).text
        return el

    def shanchu(self):
        """点击品种单边禁开配置的删除"""
        self.click(self.shanchu_element)
        return self

    def get_kejiaoyi_result(self):
        """获取到操作账户期货可交易品种/合约的实际结果"""
        Handmore = ('xpath',
                    "//td[contains(text(),'ag')]//following-sibling::td[@class='table_content_center']")
        el = self.find_element(Handmore).text
        return el

    def get_DailyCheckReport_result(self):
        """获取到核算信息页面的账户信息"""
        Handmore = ('xpath',
                    "//td[contains(text(),'账户')]//following-sibling::td[@class='table_content_center']")
        el = self.find_element(Handmore).text
        return el

    def get_LoginLogQuery_result(self):
        """获取到登录记录"""
        Handmore = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")
        el = self.find_element(Handmore).text
        return el

    def get_chanpin_result(self):
        """获取到登录记录"""
        Handmore = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")
        el = self.find_element(Handmore).text
        return el

    def HighPrice(self):
        """期货品种开仓权限详细配置输入上限"""
        self.Situation_box(self.HighPrice_element)
        self.find_element(self.HighPrice_element).send_keys('10000000')
        return self

    def LowPrice(self):
        """期货品种开仓权限详细配置输入下限"""
        self.Situation_box(self.LowPrice_element)
        self.find_element(self.LowPrice_element).send_keys('1')
        return self

    def get_pinzhongkaicang(self):
        """获取到期货品种开仓权限详细配置"""
        Handmore1 = ('xpath',
                     "//td[contains(text(),'{}')]//following-sibling::td//following-sibling::td//following-sibling::td[@class='table_content_center']".format(
                         Hadnler.yaml['contract']))

        el1 = self.find_element(Handmore1).text

        Handmore2 = ('xpath',
                     "//td[contains(text(),'{}')]//following-sibling::td[@class='table_content_center']".format(
                         Hadnler.yaml['contract']))
        el2 = self.find_element(Handmore2).text

        Handmore4 = ('xpath',
                     "//td[contains(text(),'{}')]//following-sibling::td//following-sibling::td[@class='table_content_center']".format(
                         Hadnler.yaml['contract']))
        el4 = self.find_element(Handmore4).text

        return {"方向": el2, "上限": el4, "下限": el1}

    def pinzhongkaicang_quanxuan(self):
        """点击期货品种开仓权限的全选按钮"""
        quanxuan = ('xpath', "//img[@id='all']")
        self.click(quanxuan)
        return self

    def pinzhongkaicang_shanchu(self):
        """点击期货品种开仓权限的删除按钮"""
        alldelete = ('xpath', "//span[@id='alldelete']")
        self.click(alldelete)
        return self

    def get_bangdingBZJ_result(self):
        """获取到绑定期货保证金率模板的结果"""
        Handmore = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")
        el = self.find_element(Handmore).text
        return el

    def get_bangdingSXF_result(self):
        """获取到绑定手续费率模板的结果"""
        Handmore = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")
        el = self.find_element(Handmore).text
        return el

    def get_bangdianKJYBKJYHY_result(self):
        """获取到绑定期货可交易不可交易合约模板的结果"""
        Handmore = ('xpath', "//div[@id='edittabletitle']//following-sibling::b")
        el = self.find_element(Handmore).text
        return el

    def warnHighLimit(self):
        """输入品种停板交易权限的一级风险"""
        self.find_element(self.warnHighLimit_element).send_keys('10')
        return self

    def highlimit(self):
        """输入品种停板交易权限的二级风险"""
        self.find_element(self.highlimit_element).send_keys('9')
        return self

    def exchange_CFFEX(self):
        """选择品种停板交易权限品种选择的中国金融交易所"""
        exchange_CFFEX_element = ('xpath', "//img[@id='exchange_CFFEX']")
        self.click(exchange_CFFEX_element)
        return self

    def pinzhongTBJY_quanxuan(self):
        """点击品种停板交易权限的全选按钮"""
        quanxuanF = ('xpath', "//img[@class='quanxuanF']")
        self.click(quanxuanF)
        return self

    def shanchu3(self):
        """点击删除按钮"""
        self.click(self.shanchu3_element)
        return self

    def get_pinzhongTBJY(self):
        """获取到品种停板交易权限得实际结果"""
        Handmore1 = ('xpath', "//td[@class='table_content_center']//following-sibling::td")

        el1 = self.find_element(Handmore1).text

        Handmore2 = ('xpath',
                     "//td[@class='table_content_center']//following-sibling::td//following-sibling::td")
        el2 = self.find_element(Handmore2).text

        Handmore3 = ('xpath',
                     "//td[@class='table_content_center']//following-sibling::td//following-sibling::td//following-sibling::td")
        el3 = self.find_element(Handmore3).text

        Handmore4 = ('xpath',
                     "//td[@class='table_content_center']//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td")
        el4 = self.find_element(Handmore4).text

        Handmore5 = ('xpath',
                     "//td[@class='table_content_center']//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td")
        el5 = self.find_element(Handmore5).text

        return {"类型": el1, "一级风险": el2, "一级风险触发时": el3, "二级风险": el4, "二级风险触发时": el5}

    def Varieties_limit(self):
        """点击期货品种单笔最大保证金/报单配置"""
        self.click(self.Varieties_limit_element)
        return self

    def Contract_limit(self):
        """期货合约单笔最大保证金/报单配置"""
        self.click(self.Contract_limit_element)
        return self

    def variety_select3(self):
        """期货品种单笔最大保证金/报单配置，选择品种"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        js = "document.getElementById(\"ProductID\").style.display='block'"
        self.driver.execute_script(js)
        select_elem = self.find_element(self.variety_select_element)
        select = Select(select_elem)
        select.select_by_value('TF')
        time.sleep(2)
        return self

    def bjMaxCost(self):
        """输入期货品种单笔最大保证金/报单配置的最大保证金"""
        self.Situation_box(self.bjMaxCost_element)
        self.find_element(self.bjMaxCost_element).send_keys('1000000')
        return self

    def pricepercent(self):
        """输入期货品种单笔最大保证金/报单配置的报价限制比例"""
        self.Situation_box(self.pricepercent_element)
        self.find_element(self.pricepercent_element).send_keys('50')
        return self

    def bjMaxVol(self):
        """输入期货品种单笔最大保证金/报单配置的最大报单开仓数量"""
        self.Situation_box(self.bjMaxVol_element)
        self.find_element(self.bjMaxVol_element).send_keys('10000')
        return self

    def bjCloseMaxVol(self):
        """输入期货品种单笔最大保证金/报单配置的最大报单平仓数量"""
        self.Situation_box(self.bjCloseMaxVol_element)
        self.find_element(self.bjCloseMaxVol_element).send_keys('10000')
        return self

    def OpenMinVol(self):
        """输入期货品种单笔最大保证金/报单配置的最小报单开仓数量"""
        self.Situation_box(self.OpenMinVol_element)
        self.find_element(self.OpenMinVol_element).send_keys('1')
        return self

    def CloseMinVol(self):
        """输入期货品种单笔最大保证金/报单配置的最小报单平仓数量"""
        self.Situation_box(self.CloseMinVol_element)
        self.find_element(self.CloseMinVol_element).send_keys('1')
        return self

    def get_CloseMinVol(self):
        """获取期货品种单笔最大保证金/报单配置的实际结果"""
        self.driver.switch_to.parent_frame()
        Handmore1 = ('xpath', "//td[@id='code']")

        el1 = self.find_element(Handmore1).text

        Handmore2 = ('xpath', "//td[@id='maxcost']")
        el2 = self.find_element(Handmore2).text

        Handmore3 = ('xpath', "//td[@id='maxvol']")
        el3 = self.find_element(Handmore3).text

        Handmore4 = ('xpath', "//td[@id='closemaxvol']")
        el4 = self.find_element(Handmore4).text

        Handmore5 = ('xpath', "//td[@id='pricepercent']")
        el5 = self.find_element(Handmore5).text

        Handmore6 = ('xpath', "//td[@id='openminvol']")
        el6 = self.find_element(Handmore6).text

        Handmore7 = ('xpath', "//td[@id='closeminvol']")
        el7 = self.find_element(Handmore7).text

        return {"品种/合约代码": el1, "最大保证金": el2, "最大报单开仓数量": el3, "最大报单平仓数量": el4, "报价限制比例": el5, "最小报单开仓数量": el6, "最小报单平仓数量": el7}

    def get_CloseMinVol2(self):
        """获取期货合约单笔最大保证金/报单配置的实际结果"""
        self.driver.switch_to.parent_frame()
        Handmore1 = ('xpath', "//td[@id='code']")

        el1 = self.find_element(Handmore1).text

        Handmore2 = ('xpath', "//td[@id='maxcost']")
        el2 = self.find_element(Handmore2).text

        Handmore3 = ('xpath', "//td[@id='maxvol']")
        el3 = self.find_element(Handmore3).text

        Handmore4 = ('xpath', "//td[@id='closemaxvol']")
        el4 = self.find_element(Handmore4).text

        Handmore5 = ('xpath', "//td[@id='pricepercent']")
        el5 = self.find_element(Handmore5).text

        Handmore6 = ('xpath', "//td[@id='openminvol']")
        el6 = self.find_element(Handmore6).text

        Handmore7 = ('xpath', "//td[@id='closeminvol']")
        el7 = self.find_element(Handmore7).text

        return {"品种/合约代码": el1, "最大保证金": el2, "最大报单开仓数量": el3, "最大报单平仓数量": el4, "报价限制比例": el5, "最小报单开仓数量": el6, "最小报单平仓数量": el7}

    def Added_Whitelist(self):
        """点击新增单一IP"""
        self.click(self.Added_Whitelist_element)
        return self

    def Added_Whitelist_combination(self):
        """点击新增IP段"""
        self.click(self.Added_Whitelist_combination_element)
        return self

    def opipfilter_ipbegin(self):
        """输入新增单IP"""
        self.find_element(self.opipfilter_ipbegin_element).send_keys('192.168.1.100')
        return self

    def opipfilter_ipend(self):
        """输入新增单IP-结尾"""
        self.find_element(self.opipfilter_ipend_element).send_keys('192.168.1.110')
        return self

    def get_opipfilter_ipbegin(self):
        """获取ip白名单的结果"""
        ip = ('xpath', "//td[@id='192.168.1.100']")
        el = self.find_element(ip).text
        ip2 = ('xpath', "//td[@id='192.168.1.100']//following-sibling::td")
        el2 = self.find_element(ip2).text
        return {'IP限制开始段': el, 'IP限制结束段': el2}

    def click_macipxinjian(self):
        """点击MAC地址新建"""
        self.click(self.xinjian_element)
        time.sleep(1)
        return self

    def opmacfilter_mac(self):
        """输入MAC白名单"""
        self.find_element(self.opmacfilter_mac_element).send_keys('2A-CD-C4-D7-8C-5D')
        return self

    def get_opmacfilter_mac(self):
        """获取输入的MAC白名单"""
        id_element = ('xpath', "//td[@id='2A-CD-C4-D7-8C-5D']")
        data = self.find_element(id_element).text
        return data

    def product_CF(self):
        """选择期权开仓限制管理的cf品种"""
        iframe_elem3 = self.driver.find_element_by_xpath("//iframe[@id='layui-layer-iframe1']")
        self.driver.switch_to.frame(iframe_elem3)
        self.click(self.product_CF_element)
        return self

    def get_product(self):
        """获取期权开仓限制的结果"""
        self.driver.switch_to.parent_frame()
        qlc = ('xpath', "//td[@id='qlc']")
        el = self.find_element(qlc).text
        ywc = ('xpath', "//td[@id='ywc']")
        el2 = self.find_element(ywc).text
        center = ('xpath', "//td[@align='center']")
        el3 = self.find_element(center).text
        return {'权利仓': el, '义务仓': el2, '标的品种/合约': el3}

    def delete_product_CF(self):
        """期权开仓限制管理的cf品种的全"""
        del_element = ('xpath', "//img[@class='quanxuans']")
        self.click(del_element)
        return self

    def faceoppositionlimit(self):
        """选择标的品种或者标的合约"""
        self.click(self.faceoppositionlimit_objCode)
        return self

    def xuanze_pz(self):
        """选择期权持仓量限制表管理的品种"""
        element = ('xpath', "//li[@id='objCode8IO']")
        self.click(element)
        return self

    def duotouall(self):
        """输入多头限制手数"""
        self.Situation_box(self.duotouall_element)
        self.find_element(self.duotouall_element).send_keys('10000')
        return self

    def kongtouall(self):
        """输入空头限制手数"""
        self.Situation_box(self.kongtouall_element)
        self.find_element(self.kongtouall_element).send_keys('10000')
        return self

    def get_OptPositionLimit(self):
        """获取期权持仓限制的结果"""
        result_element = ('xpath', "//td[@class='table_content_center']")
        el = self.find_element(result_element).text

        result2_element = ('xpath', "//td[@class='table_content_center']//following-sibling::td")
        el2 = self.find_element(result2_element).text

        result3_element = ('xpath', "//td[@class='table_content_center']//following-sibling::td//following-sibling::td")
        el3 = self.find_element(result3_element).text

        return {'限制的账户名': el, '限制的账户类型': el2, '标的品种或者标的合约': el3}

    def btnselectopordervolumelimit_objcode(self):
        """选择标的品种或者标的合约"""
        self.click(self.btnselectopordervolumelimit_objcode_element)
        self.click(self.objcode6IO_element)
        return self

    def btnselectopcanclevolumelimit_objcode(self):
        """选择期权撤单限制-标的品种或者标的合约"""
        self.click(self.btnselectopcanclevolumelimit_objcode_element)
        self.click(self.objcode6IO_element)
        return self

    def opcanclevolumelimit_maxcanclenumberlimitbyoneday(self):
        """输入期权撤单限制-单日最大撤单笔数限制"""
        self.Situation_box(self.opcanclevolumelimit_maxcanclenumberlimitbyoneday_element)
        self.find_element(self.opcanclevolumelimit_maxcanclenumberlimitbyoneday_element).send_keys('10000')
        return self

    def opordervolumelimit_maxmarketordervolume(self):
        """输入市价单每次最大下单手数"""
        self.Situation_box(self.opordervolumelimit_maxmarketordervolume_element)
        self.find_element(self.opordervolumelimit_maxmarketordervolume_element).send_keys('10000')
        return self

    def opordervolumelimit_maxlimitordervolume(self):
        """输入限价单每次最大下单手数"""
        self.Situation_box(self.opordervolumelimit_maxlimitordervolume_element)
        self.find_element(self.opordervolumelimit_maxlimitordervolume_element).send_keys('10000')
        return self

    def get_OptPositionLimit2(self):
        """获取期权持仓限制的结果"""
        result_element = ('xpath', "//td[@class='table_content_center']")
        el = self.find_element(result_element).text

        result2_element = ('xpath', "//td[@class='table_content_center']//following-sibling::td")
        el2 = self.find_element(result2_element).text

        result3_element = ('xpath', "//td[@class='table_content_center']//following-sibling::td//following-sibling::td")
        el3 = self.find_element(result3_element).text

        result4_element = ('xpath', "//td[@class='table_content_center']//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td")
        el4 = self.find_element(result4_element).text

        result5_element = ('xpath',
                           "//td[@class='table_content_center']//following-sibling::td//following-sibling::td//following"
                           "-sibling::td//following-sibling::td//following-sibling::td")
        el5 = self.find_element(result5_element).text

        return {'限制的账户名': el, '限制的账户类型': el2, '标的品种或者标的合约': el3, '限价单每次最大下单手数': el4, '市价单每次最大下单手数': el5}

    def get_jieguo(self):
        """获取结果"""
        result_element = ('xpath', "//td[@class='table_content']//following-sibling::td")
        el = self.find_element(result_element).text
        return el