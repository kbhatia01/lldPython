from abc import ABC, abstractmethod


class ComputerBuilder(ABC):

    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_gpu(self, gpu):
        pass

    @abstractmethod
    def set_power_supply(self, power_supply):
        pass

    @abstractmethod
    def build(self):
        pass