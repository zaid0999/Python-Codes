# Creating instance variables outside the class 

class Employee:
    pass

emp1=Employee() # Object
emp2=Employee() # Object

emp1.empno=101 # Crating instance variable
emp1.ename='naresh' # Creating instance variable
print(f'{emp1.empno},{emp1.ename}') # Accessing instance variable
emp2.empno=102 # Creating instance variable
emp2.ename='suresh' # Creating instance variable
print(f'{emp2.empno},{emp2.ename}') # Accessing instance variable