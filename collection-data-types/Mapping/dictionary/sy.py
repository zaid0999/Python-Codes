# Syntax: {key:value,key:value,key:value,….}


stud={'rollno':1,'name':'naresh','course':'python'}
print(stud,type(stud))

d2={1:'one',2:'two',3:'three'}
print(d2,type(d2))

print()

sales={2020:[5000,6000,7000],
       2021:[8000,9000,1000],
       2022:[2000,3000,4000]}
print(sales)




# 3. Creating dictionary by using existing iterables or collections
# using dict() function
# Syntax1: dict()
# Syntax2: dict(iterable/collection)
# dict() : This function creates empty dictionary


d1=dict()
print(d1,type(d1))



print("===========================================")



# dict(iterable): This function is used to convert other collections oriterables into dictionary type. Iterable must generate two valueswhile iterating or reading.


# a=[10,20,30]
# d2=dict(a)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence


b=[[1,10],[2,20],[3,30]]
d2=dict(b)
print(d2)

a1=[10,20,30]
e=enumerate(a1)
a2=dict(e)
print(a2)

print()

s=[1,2,3]
k=[10,20,30]
j=[[s[i],k[i]] for i in range(3)]
d4=dict(j)
print(d4)