class Employee:
    def __init__(self,e,en,s):
        self.__empno=e
        self.__ename=en
        self.__salary=s
    def print_employee(self):
        print(f'''EmployeeNo {self.__empno}
EmployeeName {self.__ename}
EmployeeSalary {self.__salary}''')
    def set_salary(self,s):
        self.__salary=s

emp1=Employee(101,'Zaid',60000)
emp1.print_employee()
emp1.set_salary(5000)
print("")
emp1.print_employee()