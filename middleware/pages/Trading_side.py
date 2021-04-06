
import time
import pywinauto
from pywinauto import mouse

from middleware.heandler import Hadnler
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

logging = Hadnler.logger


class TradingSide:
    """交易客户端"""

    def __init__(self, path=None, precess=None, ):
        """初始化应用程序"""
        if path:
            self.app = Application(backend='uia').start(path)
        elif precess:
            self.app = Application(backend='uia').connect(process=precess)
        self.dlg = self.app['微冲交易客户端']
        self.Order_window = None
        self.dlg_page = None

    def login(self, account, pwd):
        """登录客户端"""
        self.dlg.wait(wait_for='ready', timeout=20, retry_interval=0.5)
        # time.sleep(5)
        mouse.click(coords=(960, 433))
        send_keys('^a{}'.format(account))
        # self.dlg.print_control_identifiers()
        send_keys('{TAB}')
        send_keys(pwd)
        self.dlg['Button'].click_input()
        try:
            dlg = self.app['微冲交易客户端']['结算确认']
            dlg.wait(wait_for='ready', timeout=10, retry_interval=0.5)
            dlg.child_window(title="确认", auto_id="1", control_type="Button").click_input()
        except pywinauto.findbestmatch.MatchError as err:
            logging.info('没有找到登录后的结算确认')
        except pywinauto.timings.TimeoutError as err:
            logging.info('没有找到登录后的结算确认')
        return self

    def switching_window(self, account, name):
        """切换窗口"""
        data = '账户: {} 开户人:{} 经纪公司: ETF期权'.format(account,name)
        dlg_page = self.app[data]
        logging.info(data)
        dlg_page.wait(wait_for='ready', timeout=30, retry_interval=1)
        dlg_page.maximize()
        self.dlg_page = dlg_page
        return self

    def input_contract(self, contract):
        """输入合约号"""
        self.dlg_page.child_window(auto_id="1139", control_type="Edit").type_keys(contract)
        return self

    def input_Number(self, Number):
        """输入手数"""
        self.dlg_page.child_window(auto_id="1029", control_type="Edit").type_keys(Number)
        return self

    def input_price(self, price):
        """输入指定价"""
        self.dlg_page.child_window(auto_id="1031", control_type="Edit").set_text(price)
        return self

    def click_With_disk(self):
        """点击跟盘价改成指定价格"""
        self.dlg_page['跟盘价'].click_input()
        return self

    def click_With_assign(self):
        """点击指定价格改成跟盘价格"""
        self.dlg_page['指定价'].click_input()
        return self

    def select_deal(self, deal):
        """选择买卖"""
        self.dlg_page.child_window(auto_id="1012", control_type="ComboBox").select(deal)
        return self

    def click_place(self):
        """点击下单按钮"""
        self.dlg_page.child_window(title="下单", auto_id="1034", control_type="Button").click_input()
        return self

    def click_affirm(self):
        """下单确认按钮"""
        self.dlg_page.child_window(title="确定", auto_id="1", control_type="Button").click_input()
        return self

    def get_All_entrust(self):
        """获取全部委托的总数"""
        self.dlg_page.child_window(title=" 所有委托(F1) ", control_type="TabItem").click_input()
        data = self.dlg_page.child_window(title="Report", auto_id="1000", control_type="Table").children()
        return len(data)

    def close_client(self):
        """关闭客户端"""
        self.dlg_page.close()
        self.dlg_page['是(&Y)'].click_input()
        return self

    def unsettled(self):
        """选择未成交记录"""
        self.dlg_page.child_window(title=" 未成交记录(F4) ", control_type="TabItem").click_input()
        self.dlg_page[' 未成交记录(F4) '].print_control_identifiers()
        return self

    def unsettled_sum(self):
        """获取未成交记录的总数"""
        self.dlg_page.child_window(title=" 未成交记录(F4) ", control_type="TabItem").click_input()
        data = self.dlg_page.child_window(title="Report", auto_id="102", control_type="Table").children()
        return len(data)

    def Choose_from_single(self):
        """选择撤单(选择第一个撤单)"""
        try:
            data = self.dlg_page.child_window(title="Report", auto_id="102", control_type="Table")
            logging.info(len(data.items()))
            weizhi = data.items()[-1].rectangle().mid_point()
            mouse.double_click(coords=(weizhi.x, weizhi.y))
            return self
        except IndexError as err:
            logging.info('超出索引范围,没有这个委托')
            raise err

    def unsettled_sum2(self):
        """获取未成交记录的第一个数据的报单编号"""
        self.dlg_page.child_window(title=" 未成交记录(F4) ", control_type="TabItem").click_input()
        data = self.dlg_page.child_window(title="Report", auto_id="102", control_type="Table")
        data.print_control_identifiers()
        data = data.items()[1]
        data2 = data.children()[2].get_properties()
        return data2['texts'][0]

    def get_taxation(self):
        """获取第一个委托的报单编号"""
        self.dlg_page.child_window(title=" 所有委托(F1) ", control_type="TabItem").click_input()
        data = self.dlg_page.child_window(title="Report", auto_id="1000", control_type="Table")
        # 选择所有委托第一个最新的数据
        data = data.items()[1]
        # 获取第一个委托单下面的详细信息
        # print(data.children())
        # 获取第一个委托的报单编号
        data2 = data.children()[1].get_properties()
        return data2['texts'][0]

    def get_Position_number(self):
        """点击持仓信息并且获取持仓列表得数量"""
        self.dlg_page.child_window(title=" 持仓信息(F3) ", control_type="TabItem").click_input()
        data = self.dlg_page.child_window(title="Report", auto_id="101", control_type="Table").children()
        return len(data)

    def sale_position(self):
        """双击卖出列表第一个持仓"""
        try:
            data = self.dlg_page.child_window(title="Report", auto_id="101", control_type="Table")
            logging.info(len(data.items()))
            weizhi = data.items()[1].rectangle().mid_point()
            mouse.double_click(coords=(weizhi.x, weizhi.y))
            return self
        except IndexError as err:
            logging.info('超出索引范围,没有这个委托')
            raise err

# #
# data = TradingSide(precess='4308')
# data.switching_window('13667273351', '李秋维').click_place()


# def TradingSide2(pwd):
#     i = 71
#     while True:
#         app = Application(backend='uia').start(r'C:\Users\李秋维\Desktop\5.33.72.8\5.33.72.8.{}\RHClient.exe'.format(i))
#         dlg = app['微冲交易客户端']
#         dlg.wait(wait_for='ready', timeout=20, retry_interval=0.5)
#         # dlg['Edit'].type_keys('^a{}'.format(account))
#         # send_keys('{TAB}')
#         send_keys(pwd)
#         dlg['Button'].click_input()
#         try:
#             dlg = app['微冲交易客户端']['结算确认']
#             dlg.wait(wait_for='ready', timeout=5, retry_interval=0.5)
#             dlg.child_window(title="确认", auto_id="1", control_type="Button").click_input()
#         except pywinauto.findbestmatch.MatchError as err:
#             logging.info('没有找到登录后的结算确认')
#         except pywinauto.timings.TimeoutError as err:
#             logging.info('没有找到登录后的结算确认')
#         # if i == 150:
#         #     break
#         i += 1
#         time.sleep(30)
#         # logging.info('当前创建第{}个账号'.format(i))
#
# TradingSide2('0')
