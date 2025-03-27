# popitem()  

# Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO (Last In First Out) order. Dictionary can used to implement stack data structure. 

# If dictionary is empty, it raise KeyError

# Syntax: dictionary-name.popitem()


dict1=dict(zip("ABC",["Apple","Ball","Cat"]))
print(dict1)

item1=dict1.popitem()
print(item1)
print(dict1)

item2=dict1.popitem()
print(item2)
print(dict1)

item3=dict1.popitem()
print(item3)
print(dict1)

# item4=dict1.popitem()


