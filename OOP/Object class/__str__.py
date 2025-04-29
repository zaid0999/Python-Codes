class Employee:
    def __init__(self,e,en):
        self.__empno=e
        self.__ename=en
    def __str__(self): # Overriding method
        return f'{self.__empno,self.__ename}'
    
emp1=Employee(101,"Zaid")
print(emp1)
comp1=complex(1,2)
print(comp1)
s1=str(comp1)
print(s1,type(s1))
s2=comp1.__str__()
print(s2,type(s2))
s3=str(emp1)
print(s3,type(s3))