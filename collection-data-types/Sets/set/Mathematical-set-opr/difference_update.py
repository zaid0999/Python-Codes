# difference_update(*others) 
# set -= other | ... 
# Update the set, removing elements found in others.


a={1,2,3,4,5}
b={1,2,3,6,7}
a.difference_update(b)
print(a)