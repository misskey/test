# coding=gbk
import json
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
        res = []
        state = 0
        f = open("config.ini", "r")
        while True:
            line = f.readline()

            if line.strip():

                if line.startswith("#"):
                    pass
                if line.startswith("["):
                   pass
                if re.match(r'[^\W\d_]', line, re.U):
                     dit=self.strSpilt(line)
                     dit.pop(1)
                     print dit
            else:
                break
        f.close()
    def strSpilt(self,line):
         # PATTERN = re.compile(r"""(^\[.*?\] |".*?[^\\]?" | '.*?[^\\]?'\# | \s | \] | \[ | \, | \s= | )""", re.X)
         PATTERN = re.compile(r"""(^\[.*?\] | \: | \] | \[ | \, | \s= )""", re.X)
         return [p for p in PATTERN.split(line.strip()) if p.strip()]
    def pop(self,line):
	    if not line:
		    return False
	    val = line.pop(0)
	    return val

if __name__ == '__main__':
    fsm = FSM()
    fsm.read("")
