class Payment:
    def __init__(self, Adapter):
        self.BankAdapter = Adapter

    def checkBalance(self):
        return self.BankAdapter.checkBalance()
