A=[10,20,30,40,50]
B=iter(A)
n1=next(B)
n2=next(B)
n3=next(B)
n4=next(B)
n5=next(B)
print(n1,n2,n3,n4,n5)


print("========================")

c=list(range(10,110,10))
d=iter(c)
for value in d:
    print(value,end=' ')

print('======================')

# enumerate(iterable, start=0) 

names=["naresh","ramesh","kishore","kiran","rajesh"]

e=enumerate(names,10)
for s in e:
    print(s)

print("=================================")

sales=[50000,65000,79000,90000,85000] 
e=enumerate(sales,2010)
for s in e:
    print(s)



