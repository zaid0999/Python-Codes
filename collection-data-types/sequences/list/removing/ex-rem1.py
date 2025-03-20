# Write a program to delete al occurrences of given 
# value from list 

A=[10,50,80,30,10,70,80,10,40,50,10,20,10] 
value=10
print(f'Before Deleting{A}')
for x in A:
    if x==value:
        A.remove(value)
print(f'After Delecting {A}')
