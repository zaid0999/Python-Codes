# pop() method dictionary 
 
# Syntax: 
# pop(key[, default])

# If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised. 


d1=dict(zip("ABCDE",range(10,60,10)))
print(d1)

x=d1.pop('A')
print(x)
print(d1)

print()

y=d1.pop('E')
print(y)
print(d1)

print()

# z=d1.pop('A')


z=d1.pop('A',0)
print(z)