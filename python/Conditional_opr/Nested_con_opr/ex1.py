# Write a program to max of 3 numbers

a=int(input("Enter first integer "))
b=int(input("Enter second integer "))
c=int(input("Enter third integer "))
d=a if a>b and a>c else b if b>a and b>c else c 
print(f'Maximum of {a},{b},{c} is {d}')