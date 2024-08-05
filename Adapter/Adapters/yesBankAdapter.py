from Adapter.Adapters.BankAdapterAbc import BankAdapterAbc
from Adapter.Banks.YesBank import YesBank


class YesBankAdapter(BankAdapterAbc):
    def __init__(self):
        self.bank = YesBank()

    def checkBalance(self):
        return int(self.bank.balance())