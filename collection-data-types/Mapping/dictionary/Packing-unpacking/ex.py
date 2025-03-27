a=10,20,30,40,50
print(a,type(a))

p1,p2,p3,p4,p5=a
print(p1,p2,p3,p4,p5)

p1,p2,*p3=a
print(p1,p2,p3)

a,b,c='XYZ'
print(a,b,c)

a,b,*c='PYthon'
print(a,b,c)

pname,p=('mouse',50)
print(pname,p)

a,b,c,d,e=[10,20,30,40,50]
print(a,b,c,d,e)

a,b,*c=[10,20,30,40,50]
print(a,b,c)