# coding=gbk
__author__ = 'mgf'
__time__ = '2016/10/28'
f = open("config.ini", "r")
while True:
    line = f.readline()
    if line:
        pass    # do something here
        line=line.strip()
        p=line.rfind('.')
        filename=line[0:p]
        print line
    else:
        break
f.close()