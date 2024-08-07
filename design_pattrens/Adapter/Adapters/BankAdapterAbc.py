from abc import ABC, abstractmethod


class BankAdapterAbc(ABC):

    @abstractmethod
    def checkBalance(self):
        pass