class Person:
    def __init__(self):
        self.__name=None
    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name

class Employee:
    def __init__(self):
        self.__job=None
    def setJob(self,j):
        self.__job=j
    def getJob(self):
        return self.__job
    
class SalariedEmployee(Person,Employee):
    def __init__(self):
        Person.__init__(self)
        Employee.__init__(self)
        self.__salary=None
    def setSalary(self,s):
        self.__salary=s
    def getSalary(self):
        return self.__salary
    
emp1=SalariedEmployee()
emp1.setName("Zaid")
emp1.setJob("Manager")
emp1.setSalary(60000)
print(f'''EmployeeName: {emp1.getName()}
EmployeeJob: {emp1.getJob()}
EmployeeSalary: {emp1.getSalary()}''')