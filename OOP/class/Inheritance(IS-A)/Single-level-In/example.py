# In single level inheritance there is one base and derived classes.

# Single Level Inheitance

class Person:
    def __init__(self):
        self.__name=None
    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.__job=None
        self.__salary=None
    def setJob(self,j):
        self.__job=j
    def setSalary(self,s):
        self.__salary=s
    def getJob(self):
        return self.__job
    def getSalary(self):
        return self.__salary
    
emp1=Employee()
emp1.setName("NARESH")
emp1.setJob("Manager")
emp1.setSalary(50000)
print(f'''EmployeeName {emp1.getName()}
EmployeeJob {emp1.getJob()}
EmployeeSalary {emp1.getSalary()}''')

print("===============================")

emp1.setSalary(65000)
print(f'''EmployeeName {emp1.getName()}  
EmployeeJob {emp1.getJob()} 
EmployeeSalary {emp1.getSalary()}''') 