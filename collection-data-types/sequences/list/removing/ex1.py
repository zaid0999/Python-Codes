# Write a program to delete even numbers from list 


A=[12,2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,24,28,32,79] 
print(f'Before Deleting {A}')

i=0
l=len(A)
while i<l:
    if A[i]%2==0:
        del A[i]
        l=l-1
        continue
    i=i+1
print(f'After Deleting {A}')