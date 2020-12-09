from threading import Thread
import ctypes
import inspect

class ThreadUtil():
    def __init__(self):
        self.thread = ''

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
    import time
    def function():
        while True:
            print('线程启动成功')
            time.sleep(0.5)
    thread = ThreadUtil()
    t = thread.startThread(function)
    time.sleep(3)
    thread.stopThread(t.ident)