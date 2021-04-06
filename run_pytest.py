import os
from datetime import datetime

import pytest

ts = datetime.now().strftime("%Y-%m-%d-%H-%M%S")
# allure serve allureout


# 判断当前目录下是否存在allure测试结果集目录, 如果存在则删除
current_path = os.getcwd()
if os.path.exists(os.path.join(current_path, 'allureout')):
    results_path = os.path.join(current_path, 'allureout')
    for i in os.listdir(results_path):
        os.remove(os.path.join(results_path, i))
    os.removedirs(results_path)


if __name__ == '__main__':
    pytest.main(['--alluredir=allureout'])  # 以命令行的形式运行
    # pytest.main(['--html=output{}.html'.format(ts),'-m error'])#是、只运行error标签的用例
    # pytest.main()
1111