# coding=gbk
__author__ = 'mgf'
__time__ = '2016/10/28'
# -*- coding: utf-8 -*-
import re


def parse(s):
    l = []
    state = 0  # ״̬
    for i in s:
        if state == 0:  # ״̬Ϊ0�Ĵ���
            if 'select' in i:
                l.append(i)
                state = 1  # ״̬�ı�
            if ';' in i:
                state = 0
        elif state == 1:  # ״̬Ϊ1�Ĵ���
            l.append(i)
            if ';' in i:
                state = 0  # ״̬�ı�
    return l



