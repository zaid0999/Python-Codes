# Write a program to find max of 3 numbers using nested if
# Without using and, or operator


n1=int(input("Enter First Number "))
n2=int(input("Enter Second Number "))
n3=int(input("Enter Third Number "))

if n1==n2==n3:
    print("Equal")
elif n1>n2:
    if n1>n3:
        print(f'{n1} Is Max')
    else:
        print(f'{n3} Is Max')
elif n2>=n1:
    if n2>=n3:
        print(f'{n2} Is Max')
    else:
        print(f'{n3} Is Max')
elif n3>=n1:
    if n3>=n2:
        print(f'{n3} Is Max')
    else:
        print(f'{n2} Is Max')