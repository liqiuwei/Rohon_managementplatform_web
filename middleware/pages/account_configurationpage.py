"""操作账户配置页面"""
from middleware.pages.accountopening import AccountOpening
import time
from common.seleniunm_packaging import BasePage


class AccountConfiguration(BasePage):
    """操作账户配置页面"""
    title = '管理平台-融航商品期权资管平台'
    # 定位到修改账户
    toedit_element = ('xpath', "//a[@id='_toedit']")
    # 定位到期货合约保证金率配置
    instrumentmargin_element = ('xpath', "//a[@id='_instrumentmargin']")
    # 定位到期货品种保证金率配置
    pinzhongmargin_element = ('xpath', "//a[@id='_pinzhongmargin']")
    # 定位期货合约手续费率配置
    instrumentcommission_element = ('xpath', "//a[@id='_instrumentcommission']")
    # 定位品种手续费率配置
    productcommission_element = ('xpath', "//a[@id='_productcommission']")
    # 定位期货品种持仓配置
    productpositions_element = ('xpath', "//a[text()='期货品种持仓配置']")
    # 定位禁止品种开仓配置
    Variety_opening_prohibited_element = ('xpath', "//a[text()='禁止品种开仓配置']")
    # 定位禁止品种开仓配置
    kejiaoyi = ('xpath', "//a[text()='期货可交易品种/合约配置']")
    # 定位账户出入金配置
    churujin_element = ('xpath', "//a[@id='churujin']")
    # 定位禁止品种开仓配置
    bukejiaoyi_element = ('xpath', "//a[text()='期货不可交易品种/合约配置']")
    # 定位到核算报表查询
    DailyCheckReport_element = ("xpath", "//a[@id='_DailyCheckReport']")
    # 定位到登录日志查询
    LoginLogQuery_element = ("xpath", "//a[@id='_LoginLogQuery']")
    # 定位到绑定产品
    chanpin_element = ("xpath", "//a[@id='chanpin']")
    # 定位到期货品种开仓权限详细配置
    pinzhongkaicang_element = ("xpath", "//a[@id='pinzhongkaicang']")
    # 定位到绑定期货保证金率模板
    bangdingBZJ_element = ('xpath', "//a[@id='bangdingBZJ']")
    # 定位到绑定手续费率模板
    bangdingSXF_elemen = ('xpath', "//a[@id='bangdingSXF']")
    # 定位到绑定期货可交易不可交易合约模板
    bangdianKJYBKJYHY_elemen = ('xpath', "//a[@id='bangdianKJYBKJYHY']")
    # 定位到绑定期货品种开仓权限模板
    bangdingKCQX_elemen = ('xpath', "//a[@id='bangdingKCQX']")
    # 定位到期货品种停板交易权限
    pinzhongTBJY_element = ('xpath', "//a[@id='pinzhongTBJY']")
    # 定位到配置期货报单限制
    peizhiBD_element = ('xpath', "//a[@id='peizhiBD']")
    # 定位到期货风控方案
    fengkongFA_element = ('xpath', "//a[@id='fengkongFA']")
    # 定位到IP白名单绑定
    IPBMD_element = ('xpath', "//a[@id='IPBMD']")
    # 定位到MAC白名单绑定
    MACBMD_element = ('xpath', "//a[@id='MACBMD']")
    # 定位到期权开仓限制
    OptionOpenLimit_element = ('xpath', "//a[@id='OptionOpenLimit']")
    # 定位到期权持仓限制
    OptPositionLimit_element = ('xpath', "//a[@id='OptPositionLimit']")
    # 定位到期权下单量限制
    OrderVolumeLimit_elememt = ('xpath', "//a[@id='OrderVolumeLimit']")
    # 定位到期权下单量限制
    CancelVolumeLimit_elememt = ('xpath', "//a[@id='CancelVolumeLimit']")
    # 定位到行权记录
    ExerciseStatement_element = ('xpath', "//a[@id='ExerciseStatement']")
    # 定位到绑定期货品种持仓配置模板
    bangdingPZCC_element = ('xpath', "//a[@id='bangdingPZCC']")
    # 定位到绑定报单限制模板
    bangdingBDXZ_element = ("xpath", "//a[@id='bangdingBDXZ']")
    # 定位大到绑定期货品种停板交易权限模板
    BindingProductlimitTemplate_element = ('xpath', "//a[@id='BindingProductlimitTemplate']")
    # 定位到手续费优惠规则配置
    Shouxufeiyouhui_element = ('xpath', "//a[@id='Shouxufeiyouhui']")
    # 定位到绑定手续费优惠规则模板
    Shouxufeiyouhui2_element = ('xpath', "//a[text()='绑定手续费优惠规则模板']")


    def click_toedit(self):
        """点击修改账户"""
        self.click(self.toedit_element)
        time.sleep(1)
        return AccountOpening(self.driver)

    def click_churujin(self):
        """点击账户出入金配置"""
        self.click(self.churujin_element)
        return AccountOpening(self.driver)

    def instrumentmargin(self):
        """点击期货合约保证金率配置"""
        self.click(self.instrumentmargin_element)
        return AccountOpening(self.driver)

    def pinzhongmargin(self):
        """点击期货品种保证金率配置"""
        self.click(self.pinzhongmargin_element)
        return AccountOpening(self.driver)

    def instrumentcommission(self):
        """点击期货合约手续费率配置"""
        self.click(self.instrumentcommission_element)
        return AccountOpening(self.driver)

    def productcommission(self):
        """品种手续费率配置"""
        self.click(self.productcommission_element)
        return AccountOpening(self.driver)

    def productpositions(self):
        """期货品种持仓配置"""
        self.click(self.productpositions_element)
        return AccountOpening(self.driver)

    def Variety_opening_prohibited(self):
        """定位禁止品种开仓配置"""
        self.click(self.Variety_opening_prohibited_element)
        return AccountOpening(self.driver)

    def kejiaoyi2(self):
        """点击期货可交易品种/合约配置"""
        self.click(self.kejiaoyi)
        return AccountOpening(self.driver)

    def bukejiaoyi(self):
        """点击期货可交易品种/合约配置"""
        self.click(self.bukejiaoyi_element)
        return AccountOpening(self.driver)

    def DailyCheckReport(self):
        """点击核算报表查询"""
        self.click(self.DailyCheckReport_element)
        return AccountOpening(self.driver)

    def LoginLogQuery(self):
        """点击登录日志查询"""
        self.click(self.LoginLogQuery_element)
        return AccountOpening(self.driver)

    def chanpin(self):
        """点击绑定产品"""
        self.click(self.chanpin_element)
        return AccountOpening(self.driver)

    def pinzhongkaicang(self):
        """点击期货品种开仓权限详细配置"""
        self.click(self.pinzhongkaicang_element)
        return AccountOpening(self.driver)

    def bangdingBZJ(self):
        """点击绑定期货保证金率模板"""
        self.click(self.bangdingBZJ_element)
        return AccountOpening(self.driver)

    def bangdingSXF(self):
        """点击绑定期货保证金率模板"""
        self.click(self.bangdingSXF_elemen)
        return AccountOpening(self.driver)

    def bangdianKJYBKJYHY(self):
        """绑定期货可交易不可交易合约模板"""
        self.click(self.bangdianKJYBKJYHY_elemen)
        return AccountOpening(self.driver)

    def bangdingKCQX(self):
        """绑定期货品种开仓权限模板"""
        self.click(self.bangdingKCQX_elemen)
        return AccountOpening(self.driver)

    def pinzhongTBJY(self):
        """期货品种停板交易权限"""
        self.click(self.pinzhongTBJY_element)
        return AccountOpening(self.driver)

    def peizhiBD(self):
        """配置期货报单限制"""
        self.click(self.peizhiBD_element)
        return AccountOpening(self.driver)

    def fengkongFA(self):
        """期货风控方案"""
        self.click(self.fengkongFA_element)
        return AccountOpening(self.driver)

    def IPBMD(self):
        """定位到IP白名单绑定"""
        self.click(self.IPBMD_element)
        return AccountOpening(self.driver)

    def MACBMD(self):
        """点击MAC白名单绑定"""
        self.click(self.MACBMD_element)
        return AccountOpening(self.driver)

    def OptionOpenLimit(self):
        """点击期权开仓限制"""
        self.click(self.OptionOpenLimit_element)
        return AccountOpening(self.driver)

    def OptPositionLimit(self):
        """点击期权持仓限制"""
        self.click(self.OptPositionLimit_element)
        return AccountOpening(self.driver)

    def OrderVolumeLimit(self):
        """点击期权下单量限制"""
        self.click(self.OrderVolumeLimit_elememt)
        return AccountOpening(self.driver)

    def CancelVolumeLimit(self):
        """点击期权撤单限制"""
        self.click(self.CancelVolumeLimit_elememt)
        return AccountOpening(self.driver)

    def ExerciseStatement(self):
        """点击行权记录"""
        self.click(self.ExerciseStatement_element)
        return AccountOpening(self.driver)

    def bangdingPZCC(self):
        """点击绑定期货品种持仓配置模板"""
        self.click(self.bangdingPZCC_element)
        return AccountOpening(self.driver)

    def bangdingBDXZ(self):
        """点击绑定报单限制模板"""
        self.click(self.bangdingBDXZ_element)
        return AccountOpening(self.driver)

    def BindingProductlimitTemplate(self):
        """点击绑定期货品种停板交易权限模板"""
        self.click(self.BindingProductlimitTemplate_element)
        return AccountOpening(self.driver)

    def Shouxufeiyouhui(self):
        """点击手续费优惠规则配置"""
        self.click(self.Shouxufeiyouhui_element)
        return AccountOpening(self.driver)

    def Shouxufeiyouhui2(self):
        """点击手续费优惠规则配置"""
        self.click(self.Shouxufeiyouhui2_element)
        return AccountOpening(self.driver)
