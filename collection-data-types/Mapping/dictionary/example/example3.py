print()

employees={'naresh':60000,
           'ramesh':50000,
           'kishor':65000,
           'suresh':25000}
ename=input("Enter EmployeeName To Find Salary: ")
salary=employees.get(ename,f'{ename} not exists')
print(salary)

print()