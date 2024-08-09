from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def get_price(self):
        pass
