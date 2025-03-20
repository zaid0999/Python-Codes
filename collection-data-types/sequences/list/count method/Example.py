# Write a program to find 1 maximum value 


a=[40,20,30,50,10,10,45,50,30,45]
print(f'List is {a}')
a.sort()
print(f'First Maximum is {a[-1]}')

#  Find Second Maximum

c=a.count(a[-1])
print(f'Second Maximum is {a[-(c+1)]}')

# Find Second Minimum

c=a.count(a[0])
print(f'Second Minimum is {a[c]}')