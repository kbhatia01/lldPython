from Adapter.Adapters.IciciBankAdapter import IciciBankAdapter
from Adapter.Adapters.yesBankAdapter import YesBankAdapter
from Adapter.Phonepe import Payment

if __name__ == '__main__':
    b = YesBankAdapter()
    p = Payment(b)
    print(type(p.checkBalance()))