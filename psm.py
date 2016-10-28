# coding=gbk
__author__ = 'mgf'
__time__ = '2016/10/28'
# -*- coding: utf-8 -*-
import re


def parse(s):
    l = []
    state = 0  # 状态
    for i in s:
        if state == 0:  # 状态为0的处理
            if 'select' in i:
                l.append(i)
                state = 1  # 状态改变
            if ';' in i:
                state = 0
        elif state == 1:  # 状态为1的处理
            l.append(i)
            if ';' in i:
                state = 0  # 状态改变
    return l



