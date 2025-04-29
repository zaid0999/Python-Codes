class Person:
    def __init__(self):
        self.__name=None
    def read(self): # Overriden Method
        self.__name=input("Enter Name: ")
    def print_info(self): # Overriden Method
        print(f'Name {self.__name}')

class Student(Person):
    def __init__(self):
        super().__init__()
        self.__course=None
    def read(self): # Overriding Method
        super().read()
        self.__course=input("Enter Course: ")
    def print_info(self): # Overriding Method
        super().print_info()
        print(f'Course {self.__course}')

stud1=Student()
stud1.read()
stud1.print_info()