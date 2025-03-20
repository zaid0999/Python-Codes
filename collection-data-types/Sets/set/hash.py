# hash(object-name) 
# This hash value is used in hash based data structures for generating key. 



a=10
print(hash(a))


b=10
print(hash(b))

print(a==b)

x=1.5
y=1.5
print(x==y)

print(hash(x))
print(hash(y))



z=1.7
print(x==z)
print(hash(z))

print()


s1="abc"
s2="abc"
print(s1==s2)
print(hash(s1))
print(hash(s2))


print("========================")
t1=(10,20)
t2=(10,20)
print(t1==t2)
print(hash(t1))
print(hash(t2))
