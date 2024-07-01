from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, num_of_tires):
        self.num_of_tires = num_of_tires


    @abstractmethod
    def start(self):
        pass


# v = Vehicle(1) # error..
#
# print(v.num_of_tires)


class car(Vehicle):
    def __init__(self, num_of_tires, color):
        super().__init__(num_of_tires)
        self.color = color

    def start(self):
        print("asnc")


c = car(4, "red")
c.start()

print(c.color)


class bike(Vehicle):
    def __init__(self, num_of_tires, color):
        super().__init__(num_of_tires)
        self.color = color

    def start(self):
        print("bike started with kick..")


b = bike(2, "blue")

b.start()



class cycle(Vehicle):
    def __init__(self, num_of_tires, color):
        pass

    def start(self):
        print("started cycle..")

def startVehicle(v):
    # 1000 things... v.unlock()
    v.start()

#     1000 things..

startVehicle(b)
startVehicle(c)
cycles = cycle(1,"red")
startVehicle(cycles)




#

# def greet(hello):
#     def mfx(*args, **kwargs):
#         print("hi karan..")
#         hello(*args, **kwargs)
#         print("thanks karan..")
#
#     return mfx
#
#
# @greet
# def hello():
#     print("Hello")
#
# hello()



