import time
import datetime


class DateTimeUtil():
    def __init__(self):
        pass

    def timeStamp2date(self, timeStamp=''):
        if timeStamp == '':
            timeStamp = int(time.time())
        # # 使用time
        # timeArray = time.localtime(timeStamp)
        # date = time.strftime("%Y-%m-%d", timeArray)

        # 使用datetime
        datetimeArray = datetime.datetime.fromtimestamp(timeStamp)
        date = datetimeArray.strftime("%Y-%m-%d")
        return date

    def timeStamp2datetime(self, timeStamp=''):
        if timeStamp == '':
            timeStamp = int(time.time())
        # # 使用time
        # timeArray = time.localtime(timeStamp)
        # date_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

        # 使用datetime
        datetimeArray = datetime.datetime.fromtimestamp(timeStamp)
        date_time = datetimeArray.strftime("%Y-%m-%d %H:%M:%S")
        return date_time

    def datetime2timeStamp(self, date_time=''):
        if date_time == '':
            date_time = str(datetime.datetime.now())[:19]
        # 转为时间数组
        timeArray = time.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        # 转为时间戳
        timeStamp = int(time.mktime(timeArray))
        return timeStamp


if __name__ == '__main__':
    dtu = DateTimeUtil()
    result = dtu.datetime2timeStamp('2020-11-14 23:59:59')
    # result = dtu.timeStamp2datetime(result)
    # result = dtu.timeStamp2date()
    print(result)