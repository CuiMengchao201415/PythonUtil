from serial import Serial
import serial.tools.list_ports

from threading import Thread
import ctypes
import inspect


class SerialUtil():
    def __init__(self, port='', bps=9600, timeout=0.05):
        """
        初始化
        @param port: 串口号
        @param bps: 波特率
        @param timeout: 超时时间
        """
        self.port = port
        self.bps = bps
        self.timeout = timeout
        self.ser = None
        self.onMessage = None
        self.readType = "len"  # len or line
        self.readLen = 0  # 0或None代表读一行
        self.readLine = 0
        self.readDecodeType = None

    def getSerialParams(self, port, bps, timeout):
        """
        获取串口参数
        @param port: 串口号
        @param bps: 波特率
        @param timeout: 超时时间
        @return: 串口参数
        """
        if port == '':
            port = self.port
        if bps == '':
            bps = self.bps
        if timeout == '':
            timeout = self.timeout
        return port, bps, timeout

    def getPortList(self):
        """
        获取端口列表
        @return: 端口列表
        """
        return list(serial.tools.list_ports.comports())

    def publish(self, data='', port='', bps='', timeout=''):
        """
        发布
        @param data: 待发布数据
        @param port: 串口号
        @param bps: 波特率
        @param timeout: 超时时间
        @return:
        """
        port, bps, timeout = self.getSerialParams(port, bps, timeout)
        try:
            ser = serial.Serial(port, bps, timeout=timeout)  # 打开串口
            # 写数据
            result = ser.write(data.encode("gbk"))
            ser.close()  # 关闭串口
            return result
        except Exception as e:
            print(e)

    def subscribe(self, port='', bps='', timeout=''):
        """
        订阅
        @param port: 串口号
        @param bps: 波特率
        @param timeout: 超时时间
        @return:
        """
        port, bps, timeout = self.getSerialParams(port, bps, timeout)
        try:
            ser = serial.Serial(port, bps, timeout=timeout)
            data = ser.read(14).decode('gbk')
            ser.close()
            return data
        except Exception as e:
            print(e)

    def PubSub(self, data, port='', bps='', timeout=''):
        """
        发布订阅
        @param data: 待发布数据
        @param port: 串口号
        @param bps: 波特率
        @param timeout: 超时时间
        @return:
        """
        port, bps, timeout = self.getSerialParams(port, bps, timeout)
        try:
            ser = serial.Serial(port, bps, timeout=timeout)
            result = ser.write(data.encode("gbk"))
            data = ser.read(14).decode('gbk')
            ser.close()
            return result, data
        except Exception as e:
            print(e)

    def open(self, port='', bps='', timeout=''):
        port, bps, timeout = self.getSerialParams(port, bps, timeout)
        try:
            self.ser = serial.Serial(port, bps, timeout=timeout)
            print(f"串口端口；{port}打开成功！")
            return True
        except Exception as e:
            print(e)
            return False

    def close(self):
        try:
            if(self.ser):
                self.ser.close()
                self.ser = None
                return True
            else:
                print("串口未开启")
                return False
        except Exception as e:
            print(e)
            return False

    def pub(self, data, encodeType=None):
        if encodeType:
            data = data.encode(encodeType)
        result = self.ser.write(data)
        return result

    def sub(self, length=0, decodeType=None):
        try:
            if(length):
                data = self.ser.read(length)
            else:
                data = self.ser.readlines()[0]
            if decodeType:
                data.decode(decodeType)
            return data
        except Exception as e:
            print(e)

    def subByThreadStart(self):
        self.startThread(self.subThread)

    def subByThreadStop(self):
        self.stopThread()

    def subThread(self):
        data = None
        while True:
            if (self.ser):
                if self.readType == "len":
                    data = self.ser.read(self.readLen)
                    # if(len(data)):print(f"check:{data}")
                    if len(data) != self.readLen:
                        data = None
                        continue
                    if self.readDecodeType:
                        data.decode(self.readDecodeType)
                elif self.readType == "line":
                    data = self.ser.readlines(self.readLine)
                    if not len(data):
                        data = None
                        continue
                    if self.readDecodeType:
                        if len(data) > 1:
                            for i in range(0, len(data)):
                                data[i] = data[i].decode(self.readDecodeType)
                        else:
                            data.decode(self.readDecodeType)
                if self.onMessage:
                    self.onMessage(data)
                    data = None
            else:
                pass

    def startThread(self, function):
        """
        启动线程
        @param function: 函数
        @return: 该线程类
        """
        self.thread = Thread(target=function)
        self.thread.start()
        return self.thread

    def stopThread(self, tid=0, exc_type=SystemExit):
        """
        结束线程
        @param tid: 线程id
        @param exc_type: 执行类型
        @return:
        """
        if tid == 0:
            thread = self.thread
            tid = ctypes.c_long(thread.ident)
        if not inspect.isclass(exc_type):
            exc_type = type(exc_type)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exc_type))
        if res == 0:
            return "invalid thread id"
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            return "PyThreadState_SetAsyncExc failed"
        else:
            return "thread stop"


if __name__ == '__main__':
    su = SerialUtil()
    print(su.getPortList()[2])
