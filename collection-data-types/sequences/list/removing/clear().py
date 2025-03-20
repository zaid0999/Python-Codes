# clear() method 
# This method empty the list or remove all the values from list 
# <list-name>.clear() 


A=list(range(10,60,10))
print(A)
A.clear()
print(A)

# Using Delete Methode

b=list(range(10,110,10))
print(b)
del b[::]
print(b)