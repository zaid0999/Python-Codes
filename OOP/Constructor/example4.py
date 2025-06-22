class Complex:
    def __init__(self,r=0.0,i=0.0):
        self.real=r
        self.imag=i

comp1=Complex()
print(comp1.real,comp1.imag)
comp2=Complex(3.5,8.2)
print(comp2.real,comp2.imag)