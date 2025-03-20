# Write a program from given list read unique elements or values 
# and add inside another list

A=[1,2,3,4,5,3,3,5,6,7,8,9,7,7,9,1,2,3,11,35,11] 
B=[]

for value in A:
    if value not in B:
        B.append(value)
print(f'A List {A}')
print(f'B List{B}')