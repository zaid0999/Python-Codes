# Write a program to find minimum and maximum value in given value

a=[30,50,10,70,40,20,60]
for i in range(len(a)):
    if i==0:
        min=a[i]
        max=a[i]
    elif a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]
print(f'List is {a}')
print(f'Minimum Value is {min}')
print(f'Maximum value is {max}')