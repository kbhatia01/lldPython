from abc import ABC, abstractmethod

class Monstor(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def clone(self):
        pass