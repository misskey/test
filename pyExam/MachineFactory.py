# coding=gbk
from glob import glob
from os.path import dirname, abspath, join
from io import StringIO
import re
from datetime import datetime as dt

__author__ = 'mgf'
__time__ = '2016/10/31'
class Reader(object):

    def __init__(self, input, verbose=False):
            try:
                input.read(4)
                input.seek(0)
                self.lineFeeder = input
            except AttributeError:
                from io import StringIO
                self.lineFeeder = StringIO(unicode(input))
            global VERBOSE
            VERBOSE = verbose # be dragons

    def pop(reader, expect=None):
        # 从堆中弹出第一个.
        if not reader.line:
            return False
        val = reader.line.pop(0)
        if expect and val != expect:
            raise Exception("弹出异常 '%s'." % \
                            (val, expect))
        return val


    def top(slef,reader):
        # 忽略注释，返回下一个堆信息
        rem = reader.__next__()
        if not rem:
            line = slef._readNextLine()
            return slef.top(reader)
        return rem


    def _readNextLine(self):
        # Get next line from input.
        try:  # Turn next line into a list of tokens.
            tline = self._cleverSplit(next(self.lineFeeder))
            if not tline or tline[0] == "#":
                self.line = self._readNextLine()
            else:
                self.line = tline
        except StopIteration:
            self.line = None
        return self.line

    @staticmethod
    def _cleverSplit(line):
            # Split tokens (keeping quoted strings intact).
            PATTERN = re.compile(r"""(
                    ^\[.*?\] |						# Match Braces
                    ".*?[^\\]?" | '.*?[^\\]?' |		# Match Single/double-quotes
                    \# | 						# hash
                    \s | \] | \[ | \, | \s= |		# Whitespace, braces, comma, =
                )""", re.X)
            # Line stripping is essential for keygroup matching to work.
            if VERBOSE:
                print("token:", [p for p in PATTERN.split(line.strip()) if p.strip()])
            return [p for p in PATTERN.split(line.strip()) if p.strip()]
    def skip(self,reader, *expect):
        # 删除数据中不要的字符
        val = self.pop(reader)
        if expect and val not in expect:
            raise Exception("删除失败 '%s,'." \
                            % (val, ', '.join(expect)))
    def __next__(self):
		if not self.line or self.line[0] == "#":
			return None
		return self.line[0]

    @staticmethod
    def nextLIne(obj):
    	return obj.__next__()

    @staticmethod
    def parsePass(self):
        # 跳过此行进入下一行
        pass


    def parseKEYGROUP(self):
        symbol = self.pop(self.reader)[1:-1]
        if not symbol or symbol.isspace():
            raise Exception("Empty keygroup found.")
        self.loadKeyGroup(symbol)


    def parseASSIGN(self):
        # Parse an assignment
        # disallow variable rewriting
        var = self.pop(self.reader)  # symbol
        self.pop(self.reader, expect='=')
        val = self.parseEXP()
        if self.kgObj.get(var):
            # Disallow variable rewriting.
            raise Exception("Cannot rewrite variable: %s" % var)
        self.kgObj[var] = val


    def loadKeyGroup(self, keygroup):
        cg = self.runtime
        nlist = keygroup.split('.')
        for index, name in enumerate(nlist):
            if not name:
                raise Exception("Unexpected emtpy symbol in %s" % keygroup)
            elif not name in cg:
                cg[name] = dict()
            elif isinstance(cg[name], dict) \
                    and index == len(nlist) - 1 \
                    and self._is_pedantic:
                raise Exception("Duplicated keygroup definition: %s" % keygroup)
            cg = cg[name]
        self.kgObj = cg

    @staticmethod
    def parseEXP(self):
        # Locals are faster
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
                if next(self.reader) != ',':
                    break
                self.skip(self.reader, ",")
            self.allownl(self.reader)
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
        raise Exception("Invalid token: %s" % token)


    def allownl( self,reader):
        # If nothing left on stack, read new line.
        # Used for multiline arrays and such.
        if not reader.__next__():
            self.readLine(reader)


    def readLine(self,reader):
        # Updates line on reader and returns False if EOF is found.
        return self._readNextLine()
    def test(self):
        print "123"
    def mainLoop(self):
        print "123"
    operator={
        "skip": skip,
        "pop":pop,
        "top":top,
        "test":test,
    }
if __name__ == '__main__':
    DIR = dirname(abspath(__file__))
    tomlFile = glob(join(DIR, '*.toml'))
    for filename in tomlFile:
        with open(filename) as file:
            print("Testing file ", filename)
