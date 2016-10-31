# coding=gbk
__author__ = 'mgf'
__time__ = '2016/10/31'
class base_fsm(object):
       def enter_state(self, obj):
              raise NotImplementedError()

       def exec_state(self, obj):
              raise NotImplementedError()

       def exit_state(self, obj):
              raise NotImplementedError()