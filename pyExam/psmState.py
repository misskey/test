# -*- coding: utf-8 -*-
import re

class Parser(object):
    def __init__(self, reader, asJson=False, pedantic=True):
		self._asJson = asJson
		self._is_pedantic = pedantic
		self.reader = reader
		self.runtime = dict()
		self.kgObj = self.runtime
		self.mainLoop()
    def _readNextLine(self):
        # 获取下一行输入
        try:  # 转换为list列表
            tline = self._cleverSplit(next(self.lineFeeder))
            if not tline or tline[0] == "#":
                self.line = self._readNextLine()
            else:
                self.line = tline
        except StopIteration:
            self.line = None
        return self.line

    @staticmethod
    def modifyStates(token):
        state=1
        # 通过文件流判断字符标识
        if state==1:
            print "解析第一层"
            if token == "#":
                state="passLine"
            elif token[0] == "[":
                state="bracket"
            elif re.match(r'[^\W\d_]', token, re.U):
                state="charsNum"
            else:
                raise Exception("Unrecognized token: %s" % token)
        return state
        if state==2:
            print "解析第二层"


    def readLine(self,reader):
        return self._readNextLine()
