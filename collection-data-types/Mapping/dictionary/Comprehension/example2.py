# Write a program to read marks of n students 
# each student having name,sub1,sub2 
# organize data in dictionary 
# name is key and sub1,sub2 as values 

n=int(input("How Many Students? "))
student={input("Name "):[int(input("Sub1: ")),int(input("Sub2: "))] for i in range(n)}
print(student)
for name,marks in student.items():
    print(f'{name}==>{marks}')