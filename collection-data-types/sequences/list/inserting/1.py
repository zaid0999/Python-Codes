# Inserting values within list 
# Inserting a lows add value or element at given position or index 
# Syntax: <list-name>.insert(index,value/object) 
# Insert method of list alows inserting one value.

a=[10,20,30,40,50]
print(a)
a.insert(0,65)
print(a)

print()

a.insert(2,98)
print(a)

print()

a.insert(10,100)
print(a)

a.insert(-20,88)
print(a)

a.insert(-2,101)
print(a)

# a.insert(5,55,66)
# print(a)


print("===============================================")




# Multiple values can be inserting using slice operator 
# list-name[start-index:stop-index]=iterable 
# While inserting multiple values the start-index and stop-index must be 
# same.


a=[10,20,30,40,50]
print(a)

a[0:0]=[5,2,5,6]
print(a)

a[4:4]=[56,96]
print(a)

a[-2:-2]=[77,88]
print(a)