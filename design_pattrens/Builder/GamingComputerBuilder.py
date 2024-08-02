from ComputerBuilder import ComputerBuilder
from Computer import Computer


class GamingComputerBuilder(ComputerBuilder):

    def __init__(self, ):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.power_supply = 0
        self.storage = 0

    def set_cpu(self, cpu):
        if cpu < 2:
            raise ValueError("CPU must be at least 2")
        self.cpu = cpu

    def set_ram(self, ram):
        self.ram = ram

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_power_supply(self, power):
        self.power = power

    def set_storage(self, storage):
        self.storage = storage

    def build(self):
        c = Computer()
        c.set_cpu(self.cpu)
        c.set_ram(self.ram)
        c.set_gpu(self.gpu)
        c.set_power_supply(self.power)
        c.set_storage(self.storage)
        return c
