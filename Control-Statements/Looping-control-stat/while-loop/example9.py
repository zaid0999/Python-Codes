# Write a program to print sum of 5 numbers
# input 5 numbers from keyboard

i=1
s=0
while i<=5:
    num=int(input("Enter any number "))
    s=s+num
    i+=1

print(f'Sum is {s}')