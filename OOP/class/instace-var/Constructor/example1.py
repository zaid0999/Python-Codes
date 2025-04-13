class Employee:
    def __init__(self):
        self.empno=None
        self.ename=None
        self.salary=None

class Complex:
    def __init__(self,r=0.0,i=0.0):
        self.real=r
        self.imag=i
    
emp1=Employee()
print(emp1.empno,emp1.ename,emp1.salary)
emp2=Employee()
print(emp2.empno,emp2.ename,emp2.salary)

comp1=Complex()
print(comp1.real,comp1.imag)
comp2=Complex(1.5,2.6)
print(comp2.real,comp2.imag)

# Constructor is called only one time on object.