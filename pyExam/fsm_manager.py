# coding=gbk
from glob import glob
from os.path import dirname, abspath, join
import sys
from psmState import Parser

__author__ = 'mgf'
__time__ = '2016/11/1'
from MachineFactory import Reader


def toParse(file):
    reader =Reader(file)#读取文件流
    while reader.readLine(reader):
        token=Reader.nextLIne(reader)
        print token


if __name__ == '__main__':
     DIR = dirname(abspath(__file__))
     TOMLFiles = glob(join(DIR, '*.toml'))
     for filename in TOMLFiles:
         with open(filename) as file:
            print("Testing file ", filename)
            toParse(file)

