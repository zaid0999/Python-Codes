# Write a program to count prime numbers in given list

A=[5,8,9,12,45,78,34,98,23,21,67,54,76] 
pc=0
for value in A:
    c=0
    for i in range(1,value+1):
        if value%i==0:
            c=c+1
    if c==2:
        print(value)
        pc=pc+1
print(f'Prime Count {pc}')