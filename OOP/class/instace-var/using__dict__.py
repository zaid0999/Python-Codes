# Creating instance variables using __dict__ property or instance variable of object 

# Every object is having is a predefined instance variables caled __dict__. This variable holds instance variables or properties of object. 

# Syntax: <object-name>.__dict__={‘instance-var’:value, ‘instance-var’:value,’instance-var’:value,…} 

# Example

class Student:
    pass

stud1=Student()
stud2=Student()
stud1.rollno=1
stud1.name="naresh"
stud2.rollno=2
stud2.name="suresh"

print(stud1.__dict__)
print(stud1.rollno)
print(stud1.name)
print(stud2.__dict__)
print(stud2.rollno)
print(stud2.name)
stud3=Student()
stud3.__dict__={'rollno':3,'name':'ramesh'}
print(stud3.rollno,stud3.name)