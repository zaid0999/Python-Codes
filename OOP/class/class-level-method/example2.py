# count of instances or objects

class Employee:
    __count=0
    def __init__(self,eno,en):
        self.__empno=eno
        self.__ename=en
        Employee.__count+=1
    @classmethod
    def getEmployeeCount(cls):
        return Employee.__count
    def print_employee(self):
        print(f'''EmployeeNo {self.__empno}
              EmployeeName {self.__ename}''')
        
c=Employee.getEmployeeCount()
print(f'Count of Employees {c}')
emp1=Employee(101,"naresh")
emp2=Employee(102,"suresh")
c=Employee.getEmployeeCount()
print(f'Count of Employees {c}')
emp1.print_employee()
emp2.print_employee()