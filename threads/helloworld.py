import threading
import time


def hello_world():
    time.sleep(0.1)
    print(f"Hello World! from {threading.current_thread().name}")


thread1 = threading.Thread(target=hello_world, name="t-1")
thread2 = threading.Thread(target=hello_world, name="t-2")

thread1.start()
thread2.start()
