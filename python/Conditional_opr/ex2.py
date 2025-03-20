# write a program to find max of two nmbers

num1=int(input("Enter First Number "))
num2=int(input("Enter Second Number "))
num3=num1 if num1>num2 else num2
print(f'max of {num1} and {num2} is {num3}')