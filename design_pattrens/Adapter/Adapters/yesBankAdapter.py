from design_pattrens.Adapter.Adapters.BankAdapterAbc import BankAdapterAbc
from design_pattrens.Adapter.Banks.YesBank import YesBank


class YesBankAdapter(BankAdapterAbc):
    def __init__(self):
        self.bank = YesBank()

    def checkBalance(self):
        return int(self.bank.balance())