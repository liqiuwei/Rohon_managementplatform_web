import os

# 获取测试目录的路径
CONFIG_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASE_PATH = os.path.join(CONFIG_PATH, 'tests')

# 获取测试报告的路径
REPORTS_PATH = os.path.join(CONFIG_PATH, 'reports')

# 获取到excel路径
DATA_PATH = os.path.join(CONFIG_PATH, 'data')

# 获取到yaml文件的路径
yaml_file = os.path.join(CONFIG_PATH, 'config')
yaml_file = os.path.join(yaml_file, 'config.yaml')

# 获取到log理解路径
LOGS = os.path.join(CONFIG_PATH, 'logs')

# 获取到png路径
PNG_PATH = os.path.join(LOGS, 'pnge.png')

# 获取到识别的验证码路径
PNG_PATH_YZM = os.path.join(LOGS, 'v_code.png')
