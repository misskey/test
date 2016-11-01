# coding=gbk
__author__ = 'mgf'
__time__ = '2016/11/1'
from statemachine import StateMachine
def ones_counter(val):
    print "ONES State:    ",
    while 1:
        if val <= 0 or val >= 30:
           newState = "Out_of_Range"
           break
        else:
            print "  @ %2.1f+" % val,
    print "  >>"
    return (newState, val)

def test(val):
    print val
def test1(val):
    print val
if __name__ == '__main__':
    stat=StateMachine()
    stat.add_state("test",test)
    stat.add_state("test1",test)
    stat.set_start("test")
    stat.add_state("OUT_OF_RANGE", None, end_state=1)
    stat.run(1)