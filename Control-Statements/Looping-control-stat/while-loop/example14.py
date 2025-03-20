# Write a program to reverse number

num=int(input("Enter any number "))
rev=0
while num>0:
    d=num%10
    rev=(rev*10)+d
    num=num//10
print(f'reverse number {rev}')