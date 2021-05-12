import json

import cx_Oracle


class OracleHandler():
    """连接oracle"""
    def __init__(self, user='rhserver_WAMS8', password='rhserver_WAMS8', site='192.168.1.50'):
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

    def update(self,sql):
        """数据库更改删除语句"""
        try:
            self.cursor.execute(sql)  # 执行sql
            self.conn.commit()
            print('更改数据库语句提交成功')
        except Exception as err:
            print('更改语句提交失败')
            raise err

    def close(self):
        """关闭数据库"""
        self.cursor.close()
        self.conn.close()

    def select(self, sql):
        """json格式返回"""
        list = []
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        col_name = self.cursor.description
        for row in result:
            dict = {}
            for col in range(len(col_name)):
                key = col_name[col][0]
                value = row[col]
                dict[key] = value
            list.append(dict)
        js = json.dumps(list, ensure_ascii=False, indent=2, separators=(',', ':'))
        return js


# t_instrument 合约表
# select * from t_orderdetail t  订单详情
# select * from t_group t 产品列表
# select * from t_previousriskctrl t 风控账户管理
# select * from T_BrokenAddr 资金账户管理
# select * from t_account t 操作账户
# 成交价

data = OracleHandler().select("select * from t_account t")
print(data)
# 更改语句
# OracleHandler().update("UPDATE t_orderdetail SET STATUSMSG='测试22' where BROKERORDERSEQ='536870913'")
# 删除 语句
# OracleHandler().update("delete from t_account t where LOGINACCOUNT='104'")
#
OracleHandler().close()
