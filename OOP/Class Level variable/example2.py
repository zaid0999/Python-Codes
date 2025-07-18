class Student:
    college_name="NIT"
    def __init__(self,r,n):
        self.__rollno=r
        self.__name=n
    def print_student(self):
        print(f'Rollno{self.__rollno}')
        print(f'Name{self.__name}')
        print(f'College Name{Student.college_name}')

stud1=Student(101,'naresh')
stud1.print_student()

print("")

stud2=Student(102,'Zaid')
stud2.print_student()