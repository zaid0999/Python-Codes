# Write a program to find input number is Armstrong or not
# find 3 digit number

num=int(input("Enter any Number "))
num1=num
s=0
while num>0:
    d=num%10
    s=s+(d**3)
    num=num//10

if num1==s:
    print(f'{num1} Is Armstrong Number')
else:
    print(f'{num1} Is Not Armstrong Number')