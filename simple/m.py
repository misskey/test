# coding=gbk
__author__ = 'mgf'
__time__ = '2016/10/31'
class World(object):
       def init(self):
              self._cars = []
              self._fsm_mgr = fsm_mgr()
              self.__init_car()

       def __init_car(self):
              for i in xrange(1):   # 生产汽车
                     tmp = Car()
                     tmp.attach_fsm(0, self._fsm_mgr.get_fsm(0))
                     self._cars.append(tmp)

       def __frame(self):
              self._fsm_mgr.frame(self._cars, state_factory())

       def run(self):
              while True:
                     self.__frame()
                     sleep(0.5)
def state_factory():
       return random.randint(0, 1)
if __name__ == "__main__":
       world = World()
       world.init()
       world.run()