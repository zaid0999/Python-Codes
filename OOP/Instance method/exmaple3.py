class Student:
    def create_properties(self):
        self.rollno=1
        self.name="Zaid"
    def print_properties(self):
        print(f'Rollno {self.rollno}')
        print(f'Name {self.name}')

stud1=Student()
stud1.create_properties()
stud1.print_properties()