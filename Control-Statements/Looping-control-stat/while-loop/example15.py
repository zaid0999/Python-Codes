# Write a program to find input number is pal or not

num=int(input("Enter any number "))
num1=num
rev=0

while num>0:
    d=num%10
    rev=(rev*10)+d
    num=num//10
if rev==num1:
    print("Pal")
else:
    print("Not Pal")