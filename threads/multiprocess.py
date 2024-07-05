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

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=hello_world, args=(4,))
#

    process1.start()
# thread2.start()
# thread3.start()

    process1.join()
# thread2.join()
# thread3.join()
    time2 = time.perf_counter()

# print..
    print(time2-time1)

