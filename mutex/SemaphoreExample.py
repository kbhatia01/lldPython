from threading import *

import time

obj = Semaphore(0)
def display(name):
    obj.acquire()
    for i in range(1):
        print("Hello "+name)
        time.sleep(0.5)
    obj.release()


t1 = Thread(target=display, args=("t1",))
t2 = Thread(target=display, args=("t2",))
t3 = Thread(target=display, args=("t3",))
t4 = Thread(target=display, args=("t4",))
t5 = Thread(target=display, args=("t5",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()