import websocket
from threading import Thread
import ctypes
import inspect

class WebSocketUtil:
    def __init__(self):
        self.url = ""
        self.thread = None
        self.ws = None
        self.onOpen = None
        self.onMessage = None
        self.onError = None
        self.onClose = None

    def connect(self, url):
        self.url = url
        self.thread = Thread(target=self.wsThread)
        self.thread.start()

    def disConnect(self):
        self.stopThread()
        self.url = ""
        self.thread = None
        self.ws = None
        self.onOpen = None
        self.onMessage = None
        self.onError = None
        self.onClose = None

    def wsThread(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.url, on_open=self.on_open, on_message=self.on_message, on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever()

    def on_open(self, ws):
        if self.onOpen:
            self.onOpen(ws)

    def on_message(self, ws, message):
        if self.onMessage:
            self.onMessage(ws, message)

    def on_error(self, ws, error):
        if self.onError:
            self.onError(ws, error)

    def on_close(self, ws, code, msg):
        if self.onClose:
            self.onClose(ws, code, msg)

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


# region 单例
instance = None


def getInstance():
    global instance
    if not instance:
        instance = WebSocketUtil()
    return instance
# endregion


if __name__ == "__main__":
    def on_open(ws):
        print(f"on_open:{ws}")


    def on_message(ws, message):
        print(f"on_message:{ws}-{message}")


    def on_error(ws, error):
        print(f"on_error:{ws}-{error}")


    def on_close(ws):
        print(f"on_close:{ws}")

    wsUtil = WebSocketUtil()
    wsUtil.connect('ws://127.0.0.1:2114/webSocket/admin:1')
    wsUtil.onOpen = on_open
    wsUtil.onMessage = on_message
    wsUtil.onError = on_error
    wsUtil.onClose = on_close
    while True:
        message = input("please:")
        if (message!="q"):
            wsUtil.ws.send(message)
        else:
            wsUtil.disConnect()
            break

