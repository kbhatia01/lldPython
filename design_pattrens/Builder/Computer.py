class Computer:
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.power_supply = 0
        self.storage = 0

    def set_ram(self, ram):
        self.ram = ram

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_storage(self, storage):
        self.storage = storage

    def get_ram(self):
        return self.ram

    def set_power_supply(self, power):
        self.power_supply = power
