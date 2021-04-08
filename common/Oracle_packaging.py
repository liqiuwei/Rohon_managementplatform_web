import cx_Oracle


class OracleHandler():
    """连接oracle"""
    def __init__(self, user='rhserver_WAMS6', password='rhserver_WAMS6', site='192.168.1.50'):
        # 连接数据库 orcl
        self.conn = cx_Oracle.connect(r'{}/{}@{}/orcl'.format(user, password, site))
        # 初始化游标
        self.cursor = self.conn.cursor()

    def query(self, sql, one=False):
        """传入sql语句，返回元组格式"""
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    def query2(self, sql, one=False):
        """传入sql语句，返回是列表嵌套字典
            one=False查询全部，
            one=True查询一条
        """
        execute = self.cursor.execute(sql)
        head = execute.description
        header_list = []
        for i in head:
            header_list.append(i[0])
        lst = []
        dictionaries = {}
        if one:
            data = self.cursor.fetchone()
            for key, value in enumerate(data):
                dictionaries[header_list[key]] = value
            # lst.append(dictionaries)
            return dictionaries
        else:
            data = self.cursor.fetchall()
            for i in data:
                dictionaries = {}
                for key, value in enumerate(i):
                    dictionaries[header_list[key]] = value
                lst.append(dictionaries)
            return lst

    def close(self):
        """关闭数据库"""
        self.cursor.close()
        self.conn.close()

# select * from t_group t 产品列表
# select * from t_previousriskctrl t 风控账户管理
# select * from T_BrokenAddr 资金账户管理
# 成交价
# data = OracleHandler().query2("select * from t_group t")
# print(data)
# OracleHandler().close()
