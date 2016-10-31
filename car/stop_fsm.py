# coding=gbk
__author__ = 'mgf'
__time__ = '2016/10/31'
import base
class stop_fsm(base_fsm):
       def enter_state(self, obj):
              print "Car%s enter stop state!"%(id(obj))

       def exec_state(self, obj):
              print "Car%s in stop state!"%(id(obj))
              obj.stop()

       def exit_state(self, obj):
              print "Car%s exit stop state!"%(id(obj))