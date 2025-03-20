# Write a program to read sales of n sales persons
# and count sales>50000 and sales<50000

n=int(input("Enter how many sales persons ?"))
sales=[]
for i in range(n):
    s=float(input(f'Enter Salesperson{i+1} Sales:'))
    sales.append(s)

print(f'Sales are{sales}')
c1,c2=0,0
for s in sales:
    if s>=50000:
        c1=c1+1
    else:
        c2=c2+1
print(f'Sales count >=50000 {c1}')
print(f'Sales count <50000 {c2}')