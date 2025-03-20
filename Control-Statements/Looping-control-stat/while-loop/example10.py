# Write a program to count of digits


num=int(input("Enter any number "))
c=0
while num>0:
    c=c+1
    num=num//10
print(f'Count of digits {c}')