import sys
import time
from runTimeLogUiUtilUI import *

class RunTimeLogUiUtil(Ui_Form):
    def __init__(self, timeType='standard', path='./', filename='log.log', tempLogFilename='temp.log', runLogFilename='run.log', exceptLogFilename='except.log'):
        """
        初始化
        @param timeType: 时间格式
        @param path: 文件路径
        @param filename: 日志文件名称
        @param tempLogFilename: 临时日志文件名称
        @param runLogFilename: 运行日志文件名称
        @param exceptLogFilename: 异常日志文件名称
        """
        self.timeType = timeType
        self.path = path
        self.logFilename = filename
        self.tempLogFilename = tempLogFilename
        self.runLogFilename = runLogFilename
        self.exceptLogFilename = exceptLogFilename
        self.logFile = path + filename
        self.tempLogFile = path + tempLogFilename
        self.runLogFile = path + runLogFilename
        self.exceptLogFile = path + exceptLogFilename

        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.Form.show()

    def getDateTime(self, timeType):
        """
        根据类型返回不同类型时间参数
        @param timeType: 日期时间格式
        @return: 对应格式的时间
        """
        try:
            if timeType == '':
                timeType = self.timeType
            if timeType == 'stamp':
                return int(time.time())
            if timeType == 'msecStamp':
                return int(time.time()*1000)
            if timeType == 'standard':
                return time.strftime("%Y-%m-%d %H:%M:%S")
            if timeType == 'date':
                return time.strftime("%Y-%m-%d")
            if timeType == 'time':
                return time.strftime("%H:%M:%S")
        except:
            return ''

    def executeEvent(self, event):
        """
        要执行的事件（应重写）
        @param event: 事件
        @return:
        """
        pass

    def printLog(self, msg, timeType=''):
        """
        在控制台输出日志
        @param msg: 要输出的日志
        @param timeType: 时间格式
        @return:
        """
        try:
            log = f'{self.getDateTime(timeType)}\t{msg}'
            print(log)
            return True
        except:
            return False

    def fileLog(self, msg, event='', timeType='', path='', filename=''):
        """
        在日志文件中追加日志
        @param msg: 要输出的日志
        @param event: 要执行的事件
        @param timeType: 时间格式
        @param path: 文件路径
        @param filename: 文件名
        @return: True为成功，False为失败
        """
        try:
            if path == '' and filename == '':
                file = self.logFile
            elif path == '' and filename != '':
                file = self.path + filename
            elif path != '' and filename == '':
                file = path + self.logFilename
            else:
                file = path + filename

            log = f'{self.getDateTime(timeType)}\t{msg}\n'
            with open(file, 'a+') as fp:
                fp.write(log)

            if event:
                self.executeEvent(event)
            else:
                pass
            return True
        except:
            return False

    def tempFileLog(self, msg, event='', timeType='', path='', filename=''):
        """
        在临时日志文件中追加日志
        @param msg: 要输出的日志
        @param event: 要执行的事件
        @param timeType: 时间格式
        @param path: 文件路径
        @param filename: 文件名
        @return: True为成功，False为失败
        """
        try:
            if path == '' and filename == '':
                file = self.tempLogFile
            elif path == '' and filename != '':
                file = self.path + filename
            elif path != '' and filename == '':
                file = path + self.tempLogFilename
            else:
                file = path + filename

            log = f'{self.getDateTime(timeType)}\t{msg}\n'
            with open(file, 'a+') as fp:
                fp.write(log)

            if event:
                self.executeEvent(event)
            else:
                pass
            return True
        except:
            return False

    def runFileLog(self, msg, event='', timeType='', path='', filename=''):
        """
        在运行日志文件中追加日志
        @param msg: 要输出的日志
        @param event: 要执行的事件
        @param timeType: 时间格式
        @param path: 文件路径
        @param filename: 文件名
        @return: True为成功，False为失败
        """
        try:
            if path == '' and filename == '':
                file = self.runLogFile
            elif path == '' and filename != '':
                file = self.path + filename
            elif path != '' and filename == '':
                file = path + self.runLogFilename
            else:
                file = path + filename

            log = f'{self.getDateTime(timeType)}\t{msg}\n'
            with open(file, 'a+') as fp:
                fp.write(log)
            self.runLog_TE.append(log)

            if event:
                self.executeEvent(event)
            else:
                pass
            return True
        except:
            return False

    def exceptFileLog(self, msg, event='', timeType='', path='', filename=''):
        """
        在异常日志文件中追加日志
        @param msg: 要输出的日志
        @param event: 要执行的事件
        @param timeType: 时间格式
        @param path: 文件路径
        @param filename: 文件名
        @return: True为成功，False为失败
        """
        try:
            if path == '' and filename == '':
                file = self.exceptLogFile
            elif path == '' and filename != '':
                file = self.path + filename
            elif path != '' and filename == '':
                file = path + self.exceptLogFilename
            else:
                file = path + filename

            log = f'{self.getDateTime(timeType)}\t{msg}\n'
            with open(file, 'a+') as fp:
                fp.write(log)
            self.exceptLog_TE.append(log)

            if event:
                self.executeEvent(event)
            else:
                pass
            return True
        except:
            return False

    def readRunLog(self):
        try:
            file = self.runLogFile

            with open(file, 'r') as fp:
                log = fp.read()
            self.runLog_TE.setText(log)
        except Exception as e:
            self.exceptFileLog(f'运行日志读取出错，错误原因：{e}')

    def readExceptLog(self):
        try:
            file = self.exceptLogFile

            with open(file, 'r') as fp:
                log = fp.read()
            self.exceptLog_TE.setText(log)
        except Exception as e:
            self.exceptFileLog(f'异常日志读取出错，错误原因：{e}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    log = RunTimeLogUiUtil()
    sys.exit(app.exec_())
