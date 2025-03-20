# Write a program to replace specific value of list 
# using index

A=[10,20,30,40,50,60,70,80,90,100] 
print(f'Before Relpacing {A}')
value1=int(input("Enter value "))
value2=int(input("Enter Replace Value "))

for i in range(len(A)):
    if value1==A[i]:
        A[i]=value2
        print(f'After Replacing {A}')
        break
    else:
        print(f'{value1} not found')