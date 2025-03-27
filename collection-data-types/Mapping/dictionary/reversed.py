# reversed(dictionary) 
# This function returns reversed iterator which iterate or read keys from dictionary in reverse direction (right to left) 

# Syntax: 
# reversed(dictionary-name)


a={1:10,2:20,3:30,4:40,5:50}
print(a)

r=reversed(a)
k1=next(r)
print(k1)

k2=next(r)
print(k2)

k3=next(r)
print(k3)

k4=next(r)
print(k4)

v1=a[next(r)]
print(v1)