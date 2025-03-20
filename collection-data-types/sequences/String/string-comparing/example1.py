# write a program to count digits,alphabets,spaces,special characters 
# within string 



str1=input("Enter any String ")
dc=0
ac=0
sc=0
sp=0

for ch in str1:
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        ac+=1
    elif ch>='0' and ch<='9':
        dc+=1
    elif ch==' ':
        sc+=1
    else:
        sp+=1

print(f'Alpha Count {ac}')
print(f'Digit Count {dc}')
print(f'Space Count {sc}')
print(f'Special Character Count {sp}')