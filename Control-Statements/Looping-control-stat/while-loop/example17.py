# Write a program to convert input decimal number
# into octal number

num=int(input("Enter any number "))
octal=""

while num>7:
    d=num%8
    octal=octal+str(d)
    num=num//8
octal=octal+str(num)
print("0o"+octal[::-1])