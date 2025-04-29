# If more than one class derived from same base class, it is called hierarchical inheritance. 
class Person:
    def __init__(self):
        self.__name=None
    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name
    
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.__creaditlimit=None
    def setCreditLimit(self,c):
        self.__creaditlimit=c
    def getCreditLimit(self):
        return self.__creaditlimit

class Supplier(Person):
    def __init__(self):
        super().__init__()
        self.__address=None
    def setAddress(self,a):
        self.__address=a
    def getAddress(self):
        return self.__address
    
cust1=Customer()
cust1.setName("Naresh")
cust1.setCreditLimit(50000)
supplier=Supplier()
supplier.setName("Ramesh")
supplier.setAddress("Hyderabad")
print(f'''CustomerName: {cust1.getName()}
Customer CreditLimit: {cust1.getCreditLimit()}''')

print()

print(f'''SupplierName: {supplier.getName()}
SupplierAddress: {supplier.getAddress()}''')