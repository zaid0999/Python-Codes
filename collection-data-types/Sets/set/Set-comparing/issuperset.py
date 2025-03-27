# issuperset(other) 
# set >= other 
# Test whether every element in other is in the set. 


a={1,2,3}
b={1,2}
print(a.issuperset(b))


print()

dept10={'naresh','ramesh','suresh'} 
dept20={'naresh','suresh'}
print(dept10.issuperset(dept20))
print(dept20.issuperset(dept10))
print(dept10>=dept20)