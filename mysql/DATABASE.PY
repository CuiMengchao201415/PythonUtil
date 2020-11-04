import pymysql
import configparser
import os
from database_ui import *
class MySQL():
    def __init__(self):
        if not os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + '/database.ini'):
            with open(os.path.dirname(os.path.realpath(__file__)) + '/database.ini', 'w+') as fp:
                fp.write("[mysql]\nhost = \ndb = \nuser = \npassword = \nport = \ncharset = \nprefix = \ndatetime_format = \n")
        conf = configparser.ConfigParser()
        conf.read(os.path.dirname(os.path.realpath(__file__)) + '/database.ini', encoding="utf-8")
        mysql_items = {}
        for item in conf.items("mysql"):
            mysql_items[item[0]] = item[1]
        try:
            self.conn = pymysql.connect(host=mysql_items['host'],
                                    user=mysql_items['user'],
                                    password=mysql_items['password'],
                                    port=int(mysql_items['port']),
                                    db=mysql_items['db'],
                                    charset=mysql_items['charset'])
        except:
            Ui_Script()
            self.__init__()

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
            sql = "delete from %s where id=%d" % (table, id)
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
            sql = "select * from %s" % table
        else:
            return 'error'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def update(self, sql):
        if sql:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            return 'success'
        else:
            return 'error'

class Ui_Script(Ui_MySQL):
    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MySQL = QtWidgets.QWidget()
        self.setupUi(MySQL)
        self.config()
        MySQL.show()
        sys.exit(app.exec_())

    def config(self):
        if os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + '/database.ini'):
            conf = configparser.ConfigParser()
            conf.read(os.path.dirname(os.path.realpath(__file__)) + '/database.ini', encoding="utf-8")
            mysql_items = {}
            for item in conf.items("mysql"):
                mysql_items[item[0]] = item[1]
            self.host_LE.setText(mysql_items['host'])
            self.database_LE.setText(mysql_items['db'])
            self.username_LE.setText(mysql_items['user'])
            self.password_LE.setText(mysql_items['password'])
            self.port_LE.setText(mysql_items['port'])
            self.charset_LE.setText(mysql_items['charset'])
            self.prefix_LE.setText(mysql_items['prefix'])
            self.datetime_format_LE.setText(mysql_items['datetime_format'])
        else:
            with open(os.path.dirname(os.path.realpath(__file__)) + '/database.ini', 'w+') as fp:
                fp.write("[mysql]\nhost = \ndb = \nuser = \npassword = \nport = \ncharset = \nprefix = \ndatetime_format = \n")


    def submit(self):
        conf = configparser.ConfigParser()
        conf.read(os.path.dirname(os.path.realpath(__file__)) + '/database.ini', encoding="utf-8")
        conf.set('mysql', 'host', self.host_LE.text())
        conf.set('mysql', 'db', self.database_LE.text())
        conf.set('mysql', 'user', self.username_LE.text())
        conf.set('mysql', 'password', self.password_LE.text())
        conf.set('mysql', 'port', self.port_LE.text())
        conf.set('mysql', 'charset', self.charset_LE.text())
        conf.set('mysql', 'prefix', self.prefix_LE.text())
        # conf.set('mysql', 'datetime_format', self.datetime_format_LE.text())
        conf.write(open(os.path.dirname(os.path.realpath(__file__)) + '/database.ini', "w+", encoding="utf-8"))
        self.submit_PB.setText("保存成功")
        self.submit_PB.setEnabled(False)

if __name__ == '__main__':
    sql = MySQL()
    result = sql.select('product')
    print((result))