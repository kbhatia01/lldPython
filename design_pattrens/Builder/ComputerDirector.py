class ComputerDirector:
    def __init__(self, ComputerBuilder):
        self.ComputerBuilder = ComputerBuilder

    def construct(self):
        #  set values as per user

        self.ComputerBuilder.set_cpu(2)
        # self.ComputerBuilder.set_gpu(2)
        self.ComputerBuilder.set_ram(2)
        self.ComputerBuilder.set_storage(2)
        self.ComputerBuilder.set_power_supply(5)

    def get_computer(self):
        return self.ComputerBuilder.build()