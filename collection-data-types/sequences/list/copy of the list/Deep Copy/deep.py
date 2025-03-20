# For performing deepcopy python provides a predefined function 
# caled deepcopy()

# Syntax: 
# import copy 
# variable-name=copy.deepcopy(list-name) 



a=[10, 20, [30, 40, 50]] 
import copy
b=copy.deepcopy(a)
print(a)
print(b)

a[2].append(60)
print(a)
print(b)

b[2][0]=99
print(b)
print(a)