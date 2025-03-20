# Write a program to count of each value in a given list 


A=[1,2,3,4,5,3,3,5,6,7,8,9,7,7,9,1,2,1,3,11,35,11,35] 
B=[]
print(f'A List{A}')
for value in A:
    if value not in B:
        B.append(value)
for value in B:
    c=0
    for value1 in A:
        if value==value1:
            c+=1
    print(f'{value}==>{c}')