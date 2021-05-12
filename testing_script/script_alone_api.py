# 单独创建账号
import time

import requests
from middleware.heandler import Hadnler, OracleHandlerMid

logging = Hadnler.logger
# 输入cookie
headers = {"Cookie": "{}".format(Hadnler.yaml['Cookie'])}

#
#
# def establish_risk_control_account():
#     """创建风控制账号"""
#     setattr(Hadnler, 'digits', Hadnler().Nine_digits)
#     url = Hadnler.yaml['host'] + "riskctrlid_InsertRiskCtrlId.action"
#     data = {"riskctrlid.password": "123456",  # 风控账号的密码
#             "riskctrlid.priority": "0",
#             "riskctrlid.threeorder": "0",
#             "riskctrlid.riskmanager": "0",
#             "riskctrlid.fundmanager": "0",
#             "riskctrlid.riskctrlid": "{}".format(Hadnler.digits)  # 风控账号
#             }
#     try:
#         data = requests.request('post', url=url, data=data, headers=headers).text
#         if data == 'ok':
#             return Hadnler.digits
#         else:
#             logging.info('风控账户未创建成功')
#             return ''
#     except Exception as err:
#         logging.info('风控账户请求未成功')
#         # raise err
#
#
# def establish_product():
#     """创建产品"""
#     setattr(Hadnler, 'product_name', Hadnler().establish_product)
#     url = Hadnler.yaml['host2'] + "group_InsertGroup.action"
#     data = {"group.groupname": "{}".format(Hadnler.product_name),  # 产品名称
#             "group.synonymname": "产品别名",  # 产品别名
#             "group.subInfoType": "2",
#             "group.autoforceclosetype": "2",
#             "group.realaccountNum": "10000",
#             "group.accountNum": "10000",
#             "productmanagement": "-1",
#             "group.auto3rd": "1",
#             "pmfCollect.value": "0.00",
#             "managementcollect": "0.00",
#             "group.accesswhenonline": "0",
#             "group.accesswhennotonlinerikser": "0",
#             "group.accesswhenonlinerikser": "0",
#             "group.closeignoreexposure": "0",
#             "group.forbiddentype": "0",
#             "group.groupType": "0",
#             "group.nomoneyclosepos": "0",
#             "group.isbeforenightclosed": "0",
#             "group.equitiesAndValue": "0",
#             "group.positionAndValue": "0",
#             "group.complianceriskChild2Value": "0",
#             "group.autoprioritytype": "0",
#             "group.complianceriskChild1Value": "0",
#             "group.compliancerisk": "0",
#             "group.selectAndOr": "0",
#             "group.accesswhennotonline": "",
#             "adviserfeemethodstr": "",
#             "fundStr": "",
#             "group.closeexaminerikser": "",
#             "group.openexaminerikser": "",
#             "group.letterrecordcode": "",
#             "group.managementfeemethod": "",
#             "group.adviserfeemethod": "",
#             "real": "",
#             "group.openexamine": "",
#             "group.custodianfeemethod": "",
#             "riskStr": "",
#             "group.closeexamine": "",
#             "custodianfeemethodstr": "",
#             "group.tradingdays": "",
#             "managementfeemethodstr": "",
#             "group.productonlinedate": "",
#
#             }
#
#     data = requests.request('post', url=url, data=data, headers=headers).text
#
#     sq = "select id from t_group t where groupname='{}'".format(Hadnler.product_name)
#     data = OracleHandlerMid2().query2(sq, True)
#     return data['ID']


# def register_capital_account():
#     """注册资金账户"""
#     i = 100
#     while True:
#         setattr(Hadnler, 'capital_account', Hadnler().Nine_digits)
#         product_info = establish_product()
#         # risk_info = establish_risk_control_account()
#
#         url = Hadnler.yaml['host2'] + "realaccountinfo_InsertRealAccountInfo.action"
#         data = {"trealaccountinfo.brokenname": "模拟",  # 经纪公司
#                 "trealaccountinfo.investorname": "李秋维",  # 开户人姓名
#                 "riskCtrlID": "{},".format('FK1'),  # 选择的风控账户
#                 "nygroup": "{}".format(product_info),  # 选择的产品myvalue
#                 "trealaccountinfo.brokerid": "3030",  # 经济公司代码
#                 "trealaccount.password": "1",  # 密码
#                 "trealaccount.accounttype": "1,3,4",  # 选择的资金账户类型期货、商品期权、个股期权
#                 "trealaccount.supportshfebiglegmargin": "1",
#                 "trealaccount.supportcffexbiglegmargin": "1",
#                 "trealaccount.supportinebiglegmargin": "1",
#                 "trealaccount.priorcapital": "0.00",
#                 "trealaccountamountrelated.frozenamout": "0.00",
#                 "trealaccount.priority": "0",
#                 "trealaccount.t0": "0",
#                 "trealaccount.closeonly": "0",
#                 "trealaccountorderfrequency.closemark": "0",
#                 "trealaccount.supporthedge": "0",
#                 "trealaccountorderfrequency.timeinterval": "0",
#                 "trealaccountorderfrequency.openmark": "0",
#                 "trealaccount.iscreditacc": "0",
#                 "trealaccountorderfrequency.ordervol": "0",
#                 "cffexcode": "",
#                 "shfecode": "",
#                 "trealaccount.dynamicpwd": "",
#                 "trealaccountinfo.identifiedcardtype": "",
#                 "dcecode": ",",
#                 "trealaccountinfo.telephone": "",
#                 "trealaccountinfo.identifiedcardno": "",
#                 "czcecode": "",
#                 "inecode": "",
#                 "trealaccountamountrelated.amountshare": "",
#                 "trealaccount.userid": "",
#                 "trealaccountinfo.address": "",
#                 "trealaccountamountrelated.origamount": "",
#                 "trealaccountinfo.mobile": "",
#                 "trealaccount.tradername": "",
#                 "accountcode": "",
#                 "trealaccountinfo.investorid": "{}".format(i)  # 创建的资金账户账号
#                 }
#         i += 1
#
#         data2 = requests.request('post', url=url, data=data, headers=headers).text
#         print(i)
#         if i == 400:
#             break
# print(register_capital_account())

#
# def register_capital_account():
#     """注册资金账户"""
#     setattr(Hadnler, 'capital_account', Hadnler().Nine_digits)
#
#     # risk_info = establish_risk_control_account()
#
#     # product_info = establish_product()
#     url = Hadnler.yaml['host2'] + "realaccountinfo_InsertRealAccountInfo.action"
#     data = {"trealaccountinfo.brokenname": "模拟",  # 经纪公司
#                 "trealaccountinfo.investorname": "李秋维",  # 开户人姓名
#                 "riskCtrlID": "{},".format('FK1'),  # 选择的风控账户
#                 "nygroup": "{}".format('1016'),  # 选择的产品myvalue
#                 "trealaccountinfo.brokerid": "4080",  # 经济公司代码
#                 "trealaccount.password": "123456",  # 密码
#                 "trealaccount.accounttype": "1,3,4",  # 选择的资金账户类型期货、商品期权、个股期权
#                 "trealaccount.supportshfebiglegmargin": "1",
#                 "trealaccount.supportcffexbiglegmargin": "1",
#                 "trealaccount.supportinebiglegmargin": "1",
#                 "trealaccount.priorcapital": "0.00",
#                 "trealaccountamountrelated.frozenamout": "0.00",
#                 "trealaccount.priority": "0",
#                 "trealaccount.t0": "0",
#                 "trealaccount.closeonly": "0",
#                 "trealaccountorderfrequency.closemark": "0",
#                 "trealaccount.supporthedge": "0",
#                 "trealaccountorderfrequency.timeinterval": "0",
#                 "trealaccountorderfrequency.openmark": "0",
#                 "trealaccount.iscreditacc": "0",
#                 "trealaccountorderfrequency.ordervol": "0",
#                 "cffexcode": "",
#                 "shfecode": "",
#                 "trealaccount.dynamicpwd": "",
#                 "trealaccountinfo.identifiedcardtype": "",
#                 "dcecode": ",",
#                 "trealaccountinfo.telephone": "",
#                 "trealaccountinfo.identifiedcardno": "",
#                 "czcecode": "",
#                 "inecode": "",
#                 "trealaccountamountrelated.amountshare": "",
#                 "trealaccount.userid": "",
#                 "trealaccountinfo.address": "",
#                 "trealaccountamountrelated.origamount": "",
#                 "trealaccountinfo.mobile": "",
#                 "trealaccount.tradername": "",
#                 "accountcode": "",
#                 "trealaccountinfo.investorid": "{}".format('1')  # 创建的资金账户账号
#                 }
#
#     data = requests.request('post', url=url, data=data, headers=headers).text
#     print(data)
#
#
# register_capital_account()


e = 10
def establish_account(e=e):
    """创建操作账户"""
    # info = register_capital_account()

    while True:
        setattr(Hadnler, 'operation_account', Hadnler().mobile)
        url = Hadnler.yaml['host2'] + "account_OneKeyAccountInsert.action"
        data = {"custome.rohon_cus_credentials_type": "身份证",  # 证件类型
                "custome.rohon_cus_customename": "冯震宇",  # 开户人姓名
                "riskctrl": "{}".format('fk1'),  # 选择的风控账户
                "custome.rohon_cus_idcard": "888888888888888888",  # 证件号码
                "taccount.loginaccount": "{}".format(e),  # 操作账号
                "taccount.useorderfee": "2",
                "taccount.password": "0",  # 操作账号的密码
                "groups": "{}".format('1'),  # 选择产品
                "taccount.totalposcost": "100000000",
                "taccount.totalpositions": "100000",
                "taccount.forceclose": "-1",
                "taccount.summarylossdivtype": "-1",
                "taccount.maximumwithdrawals": "-1",
                "taccount.appendmarginrate": "-1",
                "taccount.daymaxlossforce": "-1",
                "productlimit": "-1",
                "taccount.daymaxlossnoticerate": "-1",
                "taccount.daymaxlossforcerate": "-1",
                "instrument": "-1",
                "commission": "-1",
                "taccount.daymaxlossnotice": "-1",
                "margin": "1",#选择的保证金模板
                "taccount.supportinebiglegmargin": "1",
                "taccount.supportcffexbiglegmargin": "1",
                "taccount.supportshfebiglegmargin": "1",
                "taccount.marginratiodivtype": "1",
                "taccount.daymaxlossdivtype": "1",
                "taccount.overnightmardivtype": "1",
                "taccount.orderfee": "1",
                "taccount.overnightmarclosetype": "1",
                "taccount.overnightlimittype": "1",
                "taccount.overnightmagin": "0.00",
                "taccount.overnightmaginriskrate": "0.00",
                "taccount.historymaxprofit": "0.0",
                "taccount.realcapitalamount": "0.0",
                "taccount.summarylossnoticeratio": '0',
                "taccount.commissionsetting": "0",
                "taccount.night_forceclose": "0",
                "taccount.closeday_forceclose": "0",
                "taccount.closeonly": "0",
                "amount": "0",
                "taccount.marginsetting": "1",#保证金配置  0跟随全局  1自定义
                "taccount.summarylossforceratio": "0",
                "taccountorderfrequency.closemark": "0",
                "taccount.marginratio": "0",
                "taccountorderfrequency.timeinterval": "0",
                "taccountorderfrequency.openmark": "0",
                "taccount.closeignoreexposure": "0",
                "taccount.dcesupporthedging": "0",
                "taccountorderfrequency.ordervol": "0",
                "taccount.supporthedge": "0",
                "taccount.midday_forceclose": "0",
                "taccount.isbeforenightclosed": "0",
                "ClosingCleanrance": "",
                "NightClose": "",
                "taccount.accountcode": "",
                "MiddayCloseValue": "",
                "taccount.synonymname": ""
                }
        e += 1
        data = requests.request('post', url=url, data=data, headers=headers).text
        print(data)
        print('当前创建得是{}'.format(e))
        if e == 600:
            break


establish_account()

