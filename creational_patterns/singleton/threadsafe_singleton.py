# to implemet this we have to implement thread locking so as
# to properly manage the threads


import time
from threading import Thread ,Lock
class Singleton(type):
    _instances ={}
    _lock = Lock()

    # overriding the call method
    def __call__(self, *args, **kwargs):
        # First we ensure that everything is locked :)
        with self._lock:

            if self not in self._instances:
                # craeating the instance
                instance =super().__call__(*args, **kwargs)
                time.sleep(3)
                self._instances[self] = instance

        return self._instances[self]
    
class NetworkDriver(metaclass=Singleton):
    def log(self):
        # printing the instance of my class
        print(f"{self}\n")

def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton

if __name__ == "__main__":
    # Single thread
    # s1 = create_singleton()
    # s2 = create_singleton()
    
    # Discovery the created singleton are the same for all 

    # <__main__.NetworkDriver object at 0x7fd0598c1700>

    # <__main__.NetworkDriver object at 0x7fd0598c1700>


    # Multithread

    # This ill create two singletons in two separate threads
    p1 = Thread(target=create_singleton)
    p2 = Thread(target=create_singleton)

    p1.start()
    p2.start()


# the output poses two threads of which we have a single instace
#  <__main__.NetworkDriver object at 0x7739fc28d790>
# 
# <__main__.NetworkDriver object at 0x7739fc28d7c0>
# 
# Of which this is the problem in singleton environment


# ===============SOLUTION===========================
# iNTRODUCING THREAD LOCKING 
# RESULTS:
        # <__main__.NetworkDriver object at 0x6fff7c439820>

        # <__main__.NetworkDriver object at 0x6fff7c439820>


