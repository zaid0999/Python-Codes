# remove() 
# This method is used to remove an item or value from set 
# Syntax: <set-name>.remove(value) 

# If value exists, remove method remove value from set 
# If value not exists, remove method raise KeyError



a={10,20,30,40,50}
print(a)

a.remove(20)
print(a)
a.remove(40)
print(a)
a.remove(30)
print(a)
# a.remove(40)
#  a.remove(40)
#     ~~~~~~~~^^^^
# KeyError: 40

if 40 in a:
    a.remove(40)