from abc import ABC, abstractmethod


class player(ABC):
    @abstractmethod
    def attack(self):
        pass
