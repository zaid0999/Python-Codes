# How to read content of set?



# a={10,20,30,40,50}
# print(a)
# a[0]
# TypeError: 'set' object is not subscriptable

# Set is non index colection, where reading and writing cannot done using indexing and slicing. 

# Content of set can be read using, 
# 1. for loop 
# 2. iterator 
# 3. enumerate 


# Example
# Reading content of set


a={10,20,30,40,50}

# using of loop

for value in a:
    print(value)


# using iterator

x=iter(a)
v1=next(x)
v2=next(x)
print(v1,v2)
v3=next(x)
print(v3)


print("========================")
# using enumerate

y=enumerate(a)
t1=next(y)
t2=next(y)
t3=next(y)
print(t1,t2,t3)


print()


z=enumerate(a,100)
t1=next(z)
t2=next(z)
print(t1,t2)