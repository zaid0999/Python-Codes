# Write a program to count even and odd numbers in given list

A=[2,7,5,9,12,52,65,23,33,43,12,98,67,54,67,75,45,98] 

ec=0
oc=0

for i in range(len(A)):
    if A[i]%2==0:
        ec+=1
    else:
        oc+=1
print(f'List is {A}') 
print(f'Even Number Count {ec}') 
print(f'Odd Number Count {oc}') 
