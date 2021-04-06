import os
import unittest
from libs.HTMLTestRunnerNew import HTMLTestRunner
from config import config
from datetime import datetime

# 初始化加载器
loader = unittest.TestLoader()
# 收集所有用例
test_suit = loader.discover(config.CASE_PATH)
# 设置测试报告的命名格式
ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
reports_filename = 'reports-{}.html'.format(ts)

title = '{}.融航商品期权资管平台web自动化测试报告'.format(ts)
# 测试报告的路径
reports_path = os.path.join(config.REPORTS_PATH, reports_filename)
# HTML 测试报告
with open(reports_path, 'wb') as f:
    runner = HTMLTestRunner(f, title=title, description='融航商品期权资管平台web自动化测试报告', tester='李秋维')
    runner.run(test_suit)

#练习项目

##################################循环执行脚本#####################################
# from middleware.heandler import Hadnler
# logging = Hadnler.logger
# i = 1
# while True:
#     # 初始化加载器
#     loader = unittest.TestLoader()
#     # 收集所有用例
#     test_suit = loader.discover(config.CASE_PATH)
#     # 设置测试报告的命名格式
#     ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#     reports_filename = 'reports-{}.html'.format(ts)
#
#     title = '{}.融航商品期权资管平台web自动化测试报告'.format(ts)
#     # 测试报告的路径
#     reports_path = os.path.join(config.REPORTS_PATH, reports_filename)
#     # HTML 测试报告
#     with open(reports_path, 'wb') as f:
#         runner = HTMLTestRunner(f, title=title, description='融航商品期权资管平台web自动化测试报告', tester='李秋维')
#         runner.run(test_suit)
#     if i == 70:
#         break
#     i += 1
#     logging.info('当前创建第{}个账号'.format(i))
