# Count of instances or objects

class Employee:
    __count=0
    def __init__(self,eno,en):
        self.__empno=eno
        self.__ename=en
        Employee.__count+=1
    @classmethod
    def getEmployCount(cls):
        return Employee.__count
    def print_Empoyee(self):
        print(f'''EmployeNO {self.__empno}
EmployeeName {self.__ename}''')

c=Employee.getEmployCount()
print(f'Count of Employees {c}')
emp1=Employee(101,'Naresh')
emp2=Employee(102,'Rohit')
c=Employee.getEmployCount()
print(f'Count of Employee {c}')
print()
emp1.print_Empoyee()
print()
emp2.print_Empoyee()