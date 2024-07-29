import threading


class singleton:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__new__(cls)
        return cls.__instance


if __name__ == "__main__":
    instance = singleton()
    print(instance)
    instance2 = singleton()
    print(instance2)
    print(instance is instance2)

# TODO: H.W
# Create Logger: implement singleton DP in that..
#  and TEST Above code in multithreaded env..
