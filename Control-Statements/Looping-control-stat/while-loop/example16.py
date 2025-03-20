# Write a program to convert input decimal number
# into binary number

num=int(input("Enter any number "))
b=""
while num>1:
    d=num%2
    b=b+str(d)
    num=num//2
b=b+str(num)
print("0b"+b[::-1])