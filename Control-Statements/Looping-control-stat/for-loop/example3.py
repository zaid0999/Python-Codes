# Write a program to generate factorial of input number

num=int(input("Enter any number "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f'Factorial of {num} is {fact}')