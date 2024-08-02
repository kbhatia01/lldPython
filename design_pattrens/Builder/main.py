from GamingComputerBuilder import GamingComputerBuilder
from ComputerDirector import ComputerDirector

if __name__ == '__main__':
    gb = GamingComputerBuilder()
    director = ComputerDirector(gb)
    director.construct()
    c = director.get_computer()
    print(c)
