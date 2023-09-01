
import pymysql
from comms.public_api import get_ini_data




class DBUtils:
    count = -1

    def __init__(self):
        try:
            self.conn = pymysql.connect(host=get_ini_data('mysql', 'host'),
                                        port=int(get_ini_data('mysql', 'port')),
                                        user=get_ini_data('mysql', 'user'),
                                        passwd=get_ini_data('mysql', 'pwd'),
                                        db=get_ini_data('mysql', 'db'))
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("数据库工具类连接出现异常,请检查DBUtils类中的__init__方法!")
            print(e)

    def close(self):
        self.cursor.close()
        self.conn.close()


    def cud(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            if isinstance(params, tuple):
                self.count = self.cursor.execute(sql, params)
            if isinstance(params, list):
                self.count = self.cursor.executemany(sql, params)
            self.conn.commit()
            return self.count
        except Exception as e:
            print("增删改失败!", e)


    def find_count(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            elif params is not None:
                self.count = self.cursor.execute(sql, params)
            return self.count
        except Exception as e:
            print("查询数据库条目数失败!", e)


    def find_one(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            elif params is not None:
                self.count = self.cursor.execute(sql, params)
            return self.cursor.fetchone()
        except Exception as e:
            print("查询数据库数据失败!", e)


    def find_all(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            elif params is not None:
                self.count = self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Exception as e:
            print("查询数据库数据失败!", e)


if __name__ == '__main__':
    db = DBUtils()
    CU = db.find_all('select * from my_user  ')
    print(CU)
    clo = db.close()