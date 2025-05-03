class Complex:
    def __init__(self,r=0.0,i=0.0):
        self.__real=r
        self.__imag=i
    def __str__(self):
        return f'{self.__real},{self.__imag}'
    def __add__(self,other):
        res=Complex()
        res.__real=self.__real+other.__real
        res.__imag=self.__imag+other.__imag
        return res
    
c1=Complex(1.2,1.5)
print(c1)
c2=Complex(1.6,1.8)
print(c2)
c3=c1+c2
print(c3)