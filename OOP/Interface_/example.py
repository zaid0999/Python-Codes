import abc

class Debitcard(abc.ABC):
    @abc.abstractmethod
    def withdraw(self):
        pass

class HdfcDebitcard(Debitcard):
    def withdraw(self):
        print("withdraw from HDFC Bank")

class SBIDebitcard(Debitcard):
    def withdraw(self):
        print("withdraw from SBI Bank")

class ICICIATM:
    def insert(self,d):
        d.withdraw()

atm1=ICICIATM()
card1=HdfcDebitcard()
card2=SBIDebitcard()
atm1.insert(card1)
atm1.insert(card2)