# 日志使用的封装
import logging
from config import config
import os
from common.yaml_packaging import read_yaml

# 读取yaml配置文件
logger_config = read_yaml()
# 根据key获取到字典对应的配置
log_config = logger_config['log']


def logging_pkg(name=log_config['name'],
                staream_level=log_config['staream_level'],
                file=os.path.join(config.LOGS, 'test_logs.txt')):
    # 设置日志格式
    fmt = logging.Formatter('%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s')
    # 初始化收集器
    root_logger = logging.getLogger(name)
    # 收集器设置等级
    root_logger.setLevel(staream_level)
    # 去重复日志
    root_logger.handlers.clear()
    # 初始化控制台输出
    stream_handler = logging.StreamHandler()
    # 控制台输出设置等级
    stream_handler.setLevel(staream_level)
    # 如果文件名不为None就同时创建文件输出
    if file:
        file_handler = logging.FileHandler(file, 'a', encoding='utf-8')
        file_handler.setLevel(staream_level)
        file_handler.setFormatter(fmt)
        root_logger.addHandler(file_handler)

    # 把日志格式加载到控制台输出内
    stream_handler.setFormatter(fmt)
    # 把控制台输出器放到收集器内
    root_logger.addHandler(stream_handler)
    return root_logger
