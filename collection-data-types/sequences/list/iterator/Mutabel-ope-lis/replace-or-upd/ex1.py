# Write a program to swap first and last element of list 

a=[10,20,30,40,50]
print(f'Befor Swaping {a}')

a[0],a[-1]=a[-1],a[0]
print(f'After Swaping {a}')

temp=a[0]
a[0]=a[-1]
a[-1]=temp
print(f'After Swaping{a}')