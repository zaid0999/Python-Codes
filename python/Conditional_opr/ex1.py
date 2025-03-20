# Write a program to find a person is eligible to vote

name=input("Enter Name ")
age=int(input("Enter Age "))
print(f'{name} is eligible to vote')if age>=18 else print(f'{name} is not eligible to vote')