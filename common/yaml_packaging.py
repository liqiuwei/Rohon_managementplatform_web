import yaml

# 封装读取yaml文件配置的函数
from config import config


def read_yaml(file=config.yaml_file):
    with open(file, encoding='utf-8') as f:
        conf = yaml.load(f, Loader=yaml.SafeLoader)
    return conf
