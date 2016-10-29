# -*- coding: utf-8 -*-
import re
import json
from StringIO import StringIO

VERBOSE = True
dic = dict()
val = dict()


def parseASSIGN(line):
    val = _cleverSplit(line)
    key = val.pop(0)
    val.pop(0)
    parseEXP(val)


def parseEXP(val):
    token = __next__(val)
    print token
def parseEXP(self):
		# Locals are faster
		ISO8601 = re.compile(r'^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}Z$')
		FLOAT = re.compile(r'^[+-]?\d(>?\.\d+)?$')
		STRING = re.compile(r'(?:".*?[^\\]?")|(?:\'.*?[^\\]?\')')

		token = next(self.reader)
		if token == '[':
		# Array
			array = []
			skip(self.reader, '[')
			while top(self.reader) != ']':
				array.append(self.parseEXP())
				if len(array) > 1 and self._is_pedantic\
				   and type(array[-1]) != type(array[0]):
					raise Exception("Array of mixed data types.")
				if next(self.reader) != ',':
					break
				skip(self.reader, ",")
			allownl(self.reader)
			skip(self.reader, "]")
			return array
		elif STRING.match(token):
		# String
			return pop(self.reader)[1:-1].decode('string-escape')
		elif token in ('true', 'false'):
		# Boolean
			return {'true': True, 'false': False}[pop(self.reader)]
		elif token.isdigit() or token[1:].isdigit() and token[0] in ('+', '-'):
		# Integer
			return int(pop(self.reader))
		elif FLOAT.match(token):
		# Float
			return float(pop(self.reader))
		elif ISO8601.match(token):
		# Date
			date = dt.strptime(pop(self.reader), "%Y-%m-%dT%H:%M:%SZ")
			return date if not self._asJson else date.isoformat()
		raise Exception("Invalid token: %s" % token)
def __next__(val):
		# Returns next token in the current LINE.
		# Ignores comments.
		if not val or val[0] == "#":
			return None
		return val[0]
def read(s):
    state = 0
    f = open("config.ini", "r")

    for line in f.readlines():
        if state == 0:
            if line.startswith("#"):
                pass
            if line.startswith("["):
                r = _cleverSplit(line)
                var = r[0][1:-1]
                loadKeyGroup(var)
            elif re.match(r'[^\W\d_]', line, re.U):
                vals = parseASSIGN(line)
                print vals

        elif state == 1:
            break

    f.close()


def loadKeyGroup(keygroup):
    cg = dic
    nlist = keygroup.split('.')
    for index, name in enumerate(nlist):
        if not name in cg:
            cg[name] = dict()
        cg = cg[name]


def _cleverSplit(line):
    PATTERN = re.compile(r"""(^\[.*?\] |".*?[^\\]?" | \] | \[ | \, | \s= )""", re.X)
    return [p for p in PATTERN.split(line.strip()) if p.strip()]


if __name__ == '__main__':
    input = "[servers.beta]"

    str = StringIO(unicode(input))

    read(str)

    print json.dumps(dic)
