import pymysql as ps
from pymysql import cursors


class MysqlHelper:
    
    def __init__(self, host, user, password, database, charset):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.db = None
        self.curs = None
        self.open()
    # 数据库连接
    def open(self):
        # 执行返回数据类型为字典：cursorclass =cursors.DictCursor
        self.db = ps.connect(host=self.host, user=self.user, password=self.password,database=self.database, charset=self.charset,cursorclass =cursors.DictCursor)
        self.curs = self.db.cursor()
    # 数据库关闭
    def close(self):
        self.curs.close()
        self.db.close()
    # 数据增删改
    def runCud(self, sql, params):
        try:
            self.curs.execute(sql, params)
            self.db.commit()
            print("ok")
        except :
            print('cud出现错误')
            self.db.rollback()
        
    # 数据查询,获取结果集
    def runQuery(self, sql, params):
        try:
            self.curs.execute(sql, params)
            result = self.curs.fetchall()
#             self.close()
            print("query success")
            return result
        except:
            print('query error')