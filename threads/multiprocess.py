import multiprocessing
import time

def hello_world(t):

    time.sleep(t)

    print(f"Hello World! from {multiprocessing.current_process().name}")


time1 = time.perf_counter()


#
# hello_world(4)
# hello_world(3)
# hello_world(2)
#
# process1 = multiprocessing.current_process(target=hello_world, args=[4], name="t-1")
# thread2 = threading.Thread(target=hello_world,args=[3] ,name="t-2")
# thread3 = threading.Thread(target=hello_world,args=[2] ,name="t-3")

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()
time2 = time.perf_counter()

# print..
print(time2-time1)

