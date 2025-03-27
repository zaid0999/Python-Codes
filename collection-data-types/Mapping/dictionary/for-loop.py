# for loop 
# for loop iterate/read keys from dictionary 
 
# Syntax:  
# for variable in dictionary-name: 
#       statement-1 
#       statement-2 



# Find Total Salaries

employees={'naresh':60000,
           'suresh':57000,
           'zaid':70000,
           'kishor':50000}
s=0
for name in employees:
    sal=employees[name]
    s=s+sal
    print(f'{name}==>{sal}')
print(f'Total Salaries {s}')