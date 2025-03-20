# Write a program to print sum of numbers 
# input by enduser. input numbers unitl enduser input 0

s=0
while True:
    num=int(input("Enter Any Number 0 to stop :"))
    if num==0:
        break
    s=s+num
    print(f'Sum is{s}')