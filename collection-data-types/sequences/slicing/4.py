# Write a program to print sum of elements of list

A=[10,20,30,40,50]
s=0
for value in A:
    s=value+s
print(f'List is {A}')
print(f'Sum is {s}')


# 2nd method

print("=========================")

s=0
for i in range(len(A)):
    s=s+A[i]
print(f'Sum is {s}')