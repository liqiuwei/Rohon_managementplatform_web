import os
import unittest
from libs.HTMLTestRunnerNew import HTMLTestRunner
from config import config
from datetime import datetime
from BeautifulReport import BeautifulReport
# 初始化加载器
loader = unittest.TestLoader()
# 收集所有用例
test_suit = loader.discover(config.CASE_PATH)
# 设置测试报告的命名格式
ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
reports_filename = 'reports-{}.html'.format(ts)

title = '{}.融航商品期权资管平台web自动化测试报告.html'.format(ts)
# 测试报告的路径
reports_path = os.path.join(config.REPORTS_PATH, reports_filename)
# HTML 测试报告
with open(reports_path, 'wb') as f:
    runner = HTMLTestRunner(f, title=title, description='融航商品期权资管平台web自动化测试报告\
    资管平台版本2.0.61.251\
    server版本1.6.100.158\
    交易端版本5.33.72.8', tester='李秋维')
    runner.run(test_suit)

# --------------------生成BeautifulReport测试报告-----------------------------

# br = BeautifulReport(test_suit) br.report('融航商品期权资管平台web自动化测试报告',reports_filename, report_dir=r'D:\PyCharm
# 2020.2.3\pythonProject\Rohon_managementplatform_web\reports')
