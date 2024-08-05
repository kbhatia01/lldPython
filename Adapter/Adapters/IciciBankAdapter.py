from Adapter.Adapters.BankAdapterAbc import BankAdapterAbc
from Adapter.Banks.IciciBank import IciciBank


class IciciBankAdapter(BankAdapterAbc):
    def __init__(self):
        self.bank = IciciBank()

    def checkBalance(self):
        return self.bank.bal()
