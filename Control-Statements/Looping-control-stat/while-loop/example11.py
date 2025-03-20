# Write a program to find sum of digits

num=int(input("Enter any Number "))
s=0

while num>0:
    d=num%10
    s=s+d
    num=num//10
print(f'Sum of Digits {s}')