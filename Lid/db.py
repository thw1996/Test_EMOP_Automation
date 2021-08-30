"""数据库操作"""
import logging
import pymysql
import pymssql
from Config import db_config
from Config import upload_status_sql

"""MYSQL的连接"""
class MYSQLDB(object):
    def __init__(self):
        self.conn = pymysql.connect(**db_config)
        self.cur = self.conn.cursor()

    def execute(self, sql):
        logging.debug("执行sql: {}".format(sql))
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except pymysql.err.ProgrammingError as ex:
            logging.error("sql语法错误: sql-{} 错误信息-{}".format(sql, ex))
        except pymysql.err.InternalError as ex:
            logging.error("sql执行错误: sql-{} 错误信息-{}".format(sql, ex))
        else:
            result = self.cur.fetchall()
            logging.debug("sql数据结果: {}".format(result))
            print("sql数据结果: {}".format(result))

    def close(self):
        self.cur.close()
        self.conn.close()

"""sqlserver的连接"""
class MSSQLDB(object):
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        print("已设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            print("连接数据库成功:{}".format(self.db))
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()



if __name__ == '__main__':
    ms = MSSQLDB('172.26.69.113', 'cnrem', 'P@ssw2rd', 'emop')
    resList = ms.ExecQuery("select * from tag where id = 100013")
    print(resList[0])





























