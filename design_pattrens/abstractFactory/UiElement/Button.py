from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass
