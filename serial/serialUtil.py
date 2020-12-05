from serial import Serial
import serial.tools.list_ports


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
            data = ser.read(4).decode('gbk')
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
            data = ser.read(4).decode('gbk')
            ser.close()
            return result, data
        except Exception as e:
            print(e)
