# coding=gbk
import re
from datetime import datetime as dt

__author__ = 'mgf'
__time__ = '2016/10/28'


class FSM:
    def __init__(self):
        self.dit = dict()
        self.runtime = dict()
        self.kgObj = self.runtime

    def read(self, s):
        l = []
        state = 0
        f = open("config.ini", "r")
        while True:
            line = f.readline()
            if line:
                if line.startswith("#"):
                    pass
                if line.startswith("["):
                    value = self._cleverSplit(line)
                elif re.match(r'[^\W\d_]', line, re.U):
                    value = self._cleverSplit(line)
                    v=self.__next__(value)
                    print v
            else:
                break
        f.close()
    def __next__(self,line):
            if not line or line[0] == "#":
                return None
            return line[0]
    def parseEXP(self):
        ISO8601 = re.compile(r'^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}Z$')
        FLOAT = re.compile(r'^[+-]?\d(>?\.\d+)?$')
        STRING = re.compile(r'(?:".*?[^\\]?")|(?:\'.*?[^\\]?\')')

        token = next(self.reader)
        if token == '[':
            # Array
            array = []
            self.skip(self.reader, '[')
            while self.top(self.reader) != ']':
                array.append(self.parseEXP())
                if len(array) > 1 and self._is_pedantic \
                        and type(array[-1]) != type(array[0]):
                    raise Exception("Array of mixed data types.")
                if next(self.reader) != ',':
                    break
                self.skip(self.reader, ",")
            # allownl(self.reader)
            self.skip(self.reader, "]")
            return array
        elif STRING.match(token):
            # String
            return self.pop(self.reader)[1:-1].decode('string-escape')
        elif token in ('true', 'false'):
            # Boolean
            return {'true': True, 'false': False}[self.pop(self.reader)]
        elif token.isdigit() or token[1:].isdigit() and token[0] in ('+', '-'):
            # Integer
            return int(self.pop(self.reader))
        elif FLOAT.match(token):
            # Float
            return float(self.pop(self.reader))
        elif ISO8601.match(token):
            # Date
            date = dt.strptime(self.pop(self.reader), "%Y-%m-%dT%H:%M:%SZ")
            return date if not self._asJson else date.isoformat()

    def top(self, reader):
        rem = reader.__next__()
        if not rem:
            reader._readNextLine()
        return self.top(reader)

    def skip(self, reader, *expect):
        val = self.pop(reader)

    def loadKeyGroup(self, keygroup):
        cg = self.runtime
        nlist = keygroup.split('.')
        for index, name in enumerate(nlist):
            if not name in cg:
                cg[name] = dict()
            cg = cg[name]
        self.kgObj = cg

    def _cleverSplit(self, line):
        # PATTERN = re.compile(r"""(^\[.*?\] |".*?[^\\]?" | \] | \[ | \, | \s= )""", re.X)
        PATTERN = re.compile(r"""(^\[.*?\] |".*?[^\\]?" | '.*?[^\\]?'\# | \s | \] | \[ | \, | \s= | )""", re.X)
        return [p for p in PATTERN.split(line.strip()) if p.strip()]

    def pop(self, line):
        if not line:
            return False
        val = line.pop(0)
        return val


if __name__ == '__main__':
    fsm = FSM()
    fsm.read("")
