# Write a program to sort elements of list without using 
# sort method 


n=int(input("How Many Values? "))
A=[]

for i in range(n):
    value=int(input("Enter value "))
    A.append(value)

print(f'Before Sorting {A}')

for i in range(n):
    for j in range(n-1):
        if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
print(f'After Sorting {A}')