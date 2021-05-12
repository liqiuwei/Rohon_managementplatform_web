import os
import re
from pymysql.cursors import DictCursor
from common import yaml_packaging, excel_packaging
from common.Oracle_packaging import OracleHandler
from common.logging_packaging import logging_pkg
from common.mysql_packaging import MysqlHandler
from config import config
from selenium import webdriver
import random


class MysqlHandlerMid(MysqlHandler):
    def __init__(self):
        """初始化所有的配置项从yaml中读取"""
        db_config = Hadnler.yaml['db']
        super().__init__(
            host=db_config['host'],
            port=db_config['port'],
            user=db_config['user'],
            password=db_config['password'],
            charset=db_config['charset'],
            cursorclass=DictCursor
        )


class OracleHandlerMid(OracleHandler):

    def __init__(self):
        """连接Oracle数据库"""
        db_config = Hadnler.yaml['oracledb']
        super().__init__(
            user=db_config['user'],
            password=db_config['password'],
            site=db_config['host']
        )


class Hadnler:
    """中间层"""
    # 加载配置项
    conf = config
    # 储存了MysqlHandlerMid的类
    db_class = MysqlHandlerMid
    # 获取所有的yaml配置
    yaml = yaml_packaging.read_yaml()
    # 创建资金账户
    capital_account = None
    # 报单之后的委托单
    order_ticket = None
    # 报单编号
    Entry_number = None
    # 产品名称
    product_name = None
    # 操作账户
    operation_account = None

    # db = OracleHandlerMid()
    # 获取到excel文件的所在路径
    excel_path = conf.DATA_PATH
    # 创建经纪公司
    establish_company2 = None
    # 创建的产品名称
    establish_company = None
    # 登录得账户
    login_account = None
    # 生成公司名字
    company_name = None
    # 生成人名
    name = None
    # 生成账户（电话）
    phone = None
    # 生成一键开户账户（电话）
    one__key_phone = None
    # 风控账户
    digits = None

    confirmed = None
    Strong = None
    course = None
    losses = None
    recovery = None
    ratio = None
    total = None
    flat = None

    templat_name = None

    def excel(self, file, excel_path=excel_path):
        excel = excel_packaging.ExcelHandler(os.path.join(excel_path, file))
        return excel

    # logger
    logger_config = yaml['log']
    logger = logging_pkg(name=logger_config['name'],
                         staream_level=logger_config['staream_level'],
                         file=os.path.join(conf.LOGS, 'test_logs.txt'))

    def Launch_browser(self):
        """打开浏览器"""
        import warnings
        warnings.simplefilter('ignore', ResourceWarning)  # 屏蔽报错信息
        chrome_options = webdriver.ChromeOptions()
        # 下面这行解决崩溃问题 也可能是driver和chrome不匹配
        chrome_options.add_argument('''--no-sandbox''')
        # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('''--disable-gpu''')
        driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chrome_options)
        driver.implicitly_wait(Hadnler.yaml['selenium']['time'])
        driver.maximize_window()
        return driver

    # def Launch_browser(self):
    #     """打开Edge浏览器"""
    #     import warnings
    #     warnings.simplefilter("ignore", ResourceWarning)
    #     driver = webdriver.Edge()
    #     # driver.implicitly_wait(10)
    #     # driver.maximize_window()
    #     driver.implicitly_wait(Hadnler.yaml['selenium']['time'])
    #     driver.maximize_window()
    #     return driver

    def login(self, username='admin', password='admin'):
        """登录成功"""
        from middleware.pages.login import LoginPage
        driver = self.Launch_browser()
        login = LoginPage(driver)
        login.get().login_success(username, password)
        return driver

    def capital_allocator_login(self, username, password):
        """资金调员登录"""
        from middleware.pages.homepage import IndexPage
        from middleware.pages.login import LoginPage
        driver = self.Launch_browser()
        login = LoginPage(driver)
        login.get().login_success(username, password)
        return IndexPage(driver)

    @property
    def mobile(self):
        """随机生成手机号码"""
        list = []
        while True:
            phone = '13'
            for i in range(3):
                num = random.randint(100, 900)
                phone += str(num)
            if phone not in list:
                break
        return phone

    @property
    def Nine_digits(self):
        """随机生成手机号码9位数"""
        list = []
        while True:
            digits = ''
            for i in range(3):
                num = random.randint(100, 900)
                digits += str(num)
            if digits not in list:
                break
        return digits

    def GBK2312(self):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        str = bytes.fromhex(val).decode('gb2312')
        return str

    def generate_hanzi(self):
        while True:
            hanzi = ''
            for i in range(6):
                s = self.GBK2312()
                hanzi += s
            break
        return hanzi

    def establish_company1(self):
        """创建李秋维名下的公司"""
        company = '李秋维{}公司'.format(self.generate_hanzi())
        return company

    @property
    def establish_product(self):
        """创建产品名称"""
        company = '李秋维{}产品'.format(self.generate_hanzi())
        return company

    def generate_hanzi2(self):
        """生成名字"""
        while True:
            hanzi = ''
            for i in range(3):
                s = self.GBK2312()
                hanzi += s
            break
        return hanzi

    def establish_name(self):
        """创建一个名字"""
        name = '李{}'.format(self.generate_hanzi2())
        return name

    @property
    def template_name(self):
        """创建品种开仓权限模板名称"""
        company = '{}模板'.format(self.generate_hanzi())
        return company

    def replace_data(self, data):
        """正则匹配并且替换数据"""
        patten = r"#(.*?)#"
        while re.search(patten, data):
            key = re.search(patten, data).group(1)
            value = getattr(self, key, "")
            data = re.sub(patten, str(value), data, 1)
        return data

    def random_Number(self):
        """随机生成身份证号码"""
        while True:
            list = []
            phone = ''
            for i in range(19):
                num = random.randint(0, 9)
                phone = phone + str(num)
            if not list:
                return phone

    @property
    def figure_min(self):
        """随机生成小3位数"""
        while True:
            list = []
            phone = ''
            for i in range(1):
                num = random.randint(100, 200)
                phone = phone + str(num)
            if not list:
                return phone

    @property
    def figure_max(self):
        """随机生成大3位数"""
        while True:
            list = []
            phone = ''
            for i in range(1):
                num = random.randint(201, 300)
                phone = phone + str(num)
            if not list:
                return phone

    @property
    def get_operation_account(self):
        if Hadnler.one__key_phone:
            return Hadnler.one__key_phone
        return Hadnler.yaml['operation_account']

    @property
    def get_registrant(self):
        if Hadnler.name:
            return Hadnler.name
        return Hadnler.yaml['registrant']


if __name__ == '__main__':
    pass
