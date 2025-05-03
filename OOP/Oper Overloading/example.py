class Employee:
    def __init__(self,e,en,s):
        self.__empno=e
        self.__ename=en
        self.__salary=s
    def __eq__(self,other):
        if self.__salary==other.__salary:
            return True
        else:
            return False
    def __gt__(self,other):
        return self.__salary>other.__salary
    
emp1=Employee(101,"naresh",5000)
emp2=Employee(102,"Suresh",6000)
print(emp1==emp2)
emp3=Employee(103,"kishore",5000)
print(emp1==emp3)
print(emp1>emp2)
print(emp2>emp1)