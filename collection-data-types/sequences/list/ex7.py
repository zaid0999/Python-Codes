# Write a program to count alphabets, digits and special characters in a given list


a=['1','2','A','B','$','&','*','a','b','3','4']
ac=0
dc=0
sc=0

for i in range(len(a)):
    if (a[i]>='A' and a[i]<='Z') or (a[i]>='a' and a[i]<='z'):
        ac=ac+1
    elif a[i]>='0' and a[i]<='9':
        dc=dc+1
    else:
        sc=sc+1
print(f'List is {a}')
print(f'Alphabets Count {ac}')
print(f'Digits Count {dc}')
print(f'Speacial Character Count {sc}')