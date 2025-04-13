class Student:
    def creat_properties(self):
        self.rollno=1
        self.name="naresh"
    def print_properties(self):
        print(f'Rollno: {self.rollno}')
        print(f'Name: {self.name}')

stud1=Student()
stud1.creat_properties()
stud1.print_properties()

stud2=Student()
stud2.creat_properties()
stud2.print_properties()