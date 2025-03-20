# Write a program to separate even and odd number from list 
# if number is even add inside evenlist 
# if number is odd add inside oddlist 

A=[1,2,3,4,5,6,7,10,45,82,33,77,97,37,15,51,22]
even=[]
odd=[]

for value in A:
    if value%2==0:
        even.append(value)
    else:
        odd.append(value)
print(f'List is =>{A}')
print(f'Even list is =>{even}')
print(f'Odd list is =>{odd}')