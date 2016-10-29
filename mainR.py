# coding=gbk
__author__ = 'mgf'
__time__ = '2016/10/28'


class FSM:
    def read(s):
        l = []
        state = 0
        f = open("config.ini", "r")
        while True:
            line = f.readline()
            if line:
                if line.startswith("#"):
                    pass
                if line.startswith("["):
                   FSM.pop(line)[1:-1]
            else:
                break
        f.close()

    def pop(reader, expect=None):
        if not reader.line:
            return False
        val = reader.line.pop(0)
        return val

    if __name__ == '__main__':
        read("")
