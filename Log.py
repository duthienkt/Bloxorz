__PROCESSING__ = False
if __PROCESSING__:
    from PDefine import *

MESS = 1
ERROR = 2
NOTICE = 3


class Log:
    data = []

    @staticmethod
    def mess(obj):
        Log.data.append([MESS, str(obj)])

    @staticmethod
    def notice(obj):
        Log.data.append([NOTICE, str(obj)])

    @staticmethod
    def error(obj):
        Log.data.append([ERROR, str(obj)])

    @staticmethod
    def draw():
        noStroke()
        fill(0)
        textSize(13)
        y = 15
        l = len(Log.data)
        i = l - 35
        if i < 0:
            i = 0
        while i < l:
            line_data = Log.data[i]
            if line_data[0] == MESS:
                fill(0)
            if line_data[0] == ERROR:
                fill(255, 0, 0)
            if line_data[0] == NOTICE:
                fill(255, 255, 0)

            text(line_data[1], 10, y)
            y += 20
            i = i + 1

    @staticmethod
    def save(p):
        data = []
        for i in range(len(Log.data)):
            data.append(Log.data[i][1])
        # Log.error(data)
        saveStrings(p, data)


