# Python Set difference to find lost element from a 
# duplicated array 

a = [1, 4, 5, 7, 9, 2] 
b = [4, 5, 7, 9]

c=set(a)-set(b)
print(a)
print(b)
print(list(c))