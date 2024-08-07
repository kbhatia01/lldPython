from design_pattrens.Adapter.Adapters.BankAdapterAbc import BankAdapterAbc
from design_pattrens.Adapter.Banks.IciciBank import IciciBank


class IciciBankAdapter(BankAdapterAbc):
    def __init__(self):
        self.bank = IciciBank()

    def checkBalance(self):
        return self.bank.bal()
