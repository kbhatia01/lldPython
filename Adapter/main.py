from Adapter.Adapters.IciciBankAdapter import IciciBankAdapter
from Adapter.Adapters.yesBankAdapter import YesBankAdapter
from Adapter.Phonepe import PhonePe

if __name__ == '__main__':
    b = YesBankAdapter()
    p = PhonePe(b)
    print(type(p.checkBalance()))