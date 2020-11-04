import pymysql
import configparser
import os
import pandas as pd

class MySqlUtil():
    def __init__(self):
        try:
            if not os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + '/database.ini'):
                with open(os.path.dirname(os.path.realpath(__file__)) + '/database.ini', 'w+') as fp:
                    fp.write(
                        "[mysql]\nhost = \ndb = \nuser = \npassword = \nport = \ncharset = \n")
            conf = configparser.ConfigParser()
            conf.read(os.path.dirname(os.path.realpath(__file__)) + '/database.ini', encoding="utf-8")
            mysql_items = {}
            for item in conf.items("mysql"):
                mysql_items[item[0]] = item[1]
            # 连接database
            self.conn = pymysql.connect(host=mysql_items['host'],
                                        user=mysql_items['user'],
                                        password=mysql_items['password'],
                                        port=int(mysql_items['port']),
                                        db=mysql_items['db'],
                                        charset=mysql_items['charset'])
            try:
                self.prefix = mysql_items['prefix']
            except:
                self.prefix = ''
        except Exception:
            print('数据库配置有误')
            os._exit(0)

    def createtable(self, sql):
        if sql:
            cursor = self.conn.cursor(buffered=True)
            cursor.execute(sql)
            cursor.close()
            return 'success'
        else:
            return 'error'

    def insert(self, sql):
        if sql:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.close()
            return 'success'
        else:
            return 'error'

    def delete(self, id, table='', sql=''):
        if sql:
            sql = sql
        elif table:
            sql = "delete from %s where id=%d" % (self.prefix+table, id)
        else:
            return 'error'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        return 'success'

    def select(self, table='', sql=''):
        if sql:
            sql = sql
        elif table:
            sql = "select * from %s" % self.prefix+table
        else:
            return 'error'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def dbselect(self, sql=''):
        try:
            result = pd.read_sql(sql, self.conn)
            return result
        except:
            return 'error'

    def update(self, sql):
        if sql:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            return 'success'
        else:
            return 'error'


if __name__ == '__main__':
    mysql = MySqlUtil()
    result = mysql.select(sql="select * from zxcms_admin")
    print(result)
