# Update() method 
# This method adds or updates more than one item of dictionary

# Syntax: dictionary-name.update(iterable)

# Update method required iteable, which generates key and value 


d1={1:10,2:20}
print(d1)

print()

d1.update({3:30,4:40,5:50})
print(d1)

print()

d1.update({1:100,2:200,6:60})
print(d1)

print()

d1.update(zip(range(7,11),range(70,110,10)))
print(d1)

print()