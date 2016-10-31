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
