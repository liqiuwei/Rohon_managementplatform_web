import pymysql
from pymysql.cursors import DictCursor
from common.yaml_packaging import read_yaml

data = read_yaml()
datas = data['db']


class MysqlHandler():
    def __init__(self,
                 host=datas['host'],
                 port=3306,
                 user=datas['user'],
                 password=datas['password'],
                 charset='utf8',
                 cursorclass=DictCursor
                 ):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,
            cursorclass=cursorclass
        )
        # 对象初始化游标
        self.cursor = self.conn.cursor()

    def query(self, sql, one=True):
        """传入sql语句"""
        self.conn.commit()  # 每次查询数据之前都对数据库进行更新
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

