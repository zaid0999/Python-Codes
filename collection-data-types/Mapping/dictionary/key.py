# Using key 
# Dictionary is a key based colection and we can read content using key. 
# Syntax:  dictionary-name[key] 
# If key exists, it read value 
# If key not exists, it raises KeyError


users={'naresh':'nit123',
       'sursh':'s123',
       'ramesh':'r123'}
print('naresh' in users)
print('ramesh' in users)
print('zaid' in users)


print("==========================")

# Note: Dictionary allows duplicate values but does not duplicate keys 


d1={1:10,2:20,3:30}
print(d1)

print()

d2={1:10,1:20,1:30}
print(d2)