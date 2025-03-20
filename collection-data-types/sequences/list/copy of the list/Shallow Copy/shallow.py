# Shallow Copy 
# copy() method of list create shallow copy of list. 


a=[10,20,30,40]
b=a.copy()
print(a)
print(b)

print("====================")

x=[10,[20,30]]
y=x.copy()
x[1].append(40)
print(x)
print(y)
x[1][2]=99
print(x)

print("========================================================")
print("========================================================")

# Without copy method shalow copy is done using slice operator 

p=[10,[20,30]]
q=p[:]
print(p)
print(q)

p[1][0]=44
print(p)
print(q)


print("****************************************")

# Another method of shalow copy without using copy() method 

a=[10,20,30,40,50]
b=list(a)
print(id(a))
print(id(b))

print()

x==[10,20,[30,40]]

y=list(x)
print(id(x))
print(id(y))
print(id(x[1]))
print(id(y[1]))