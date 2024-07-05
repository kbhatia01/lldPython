import threading
import concurrent.futures
import time


def hello_world(t):

    time.sleep(t)

    return f"Hello World! from {threading.current_thread().name}"



time1 = time.perf_counter()


#
# hello_world(4)
# hello_world(3)
# hello_world(2)
with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
    f1 = executor.submit(hello_world, 4) # T1 T1 T1 T1
    f2 = executor.submit(hello_world, 3) # T2 T2 T2
    f3 = executor.submit(hello_world, 2) # Q  Q  Q  T2 T2

    result3 = f3.result()
    print(result3)

    result1  = f1.result()
    result2 = f2.result()

    print(result1)
    print(result2)



    # print(val,val2,val3)





# thread1 = threading.Thread(target=hello_world, args=[4], name="t-1")
# thread2 = threading.Thread(target=hello_world,args=[3] ,name="t-2")
# thread3 = threading.Thread(target=hello_world,args=[2] ,name="t-3")

# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
time2 = time.perf_counter()

# print..
print(time2-time1)
