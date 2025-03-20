# Write a program to print sum of list elements

A=[10,20,30,40,50,60,70,80,90,100]
s=0

for i in range(len(A)):
    s=s+A[i]
print(f'List{A}')
print(f'Sum of elements {s}')