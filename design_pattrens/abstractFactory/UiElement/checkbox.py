from abc import ABC, abstractmethod

class Checkbox(ABC):
    @abstractmethod
    def click(self):
        pass
