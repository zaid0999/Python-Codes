# del keyword 

# “del” keyword required “key” for deleting items from dictionary 

# Syntax: del dictionary-name[key] 

# If key exists within dictionary, it deletes item 
# If key not exists within dictionary, it raises KeyError 

# Note: to avoid KeyError, search before deleting item 



d1=dict(zip(range(1,8),range(10,80,10)))
print(d1)

print()

del d1[2]
print(d1)

print()

del d1[6]
print(d1)

print()

# del d1[8]
# print(d1)