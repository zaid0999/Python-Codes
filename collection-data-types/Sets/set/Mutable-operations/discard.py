# discard()  
# This method is used to remove or delete an item from set 
# This method does not raise any error if value not exists within set 

# Syntax: <set-name>.discard(value) 


a={10,20,30,40,50}
print(a)

a.discard(10)
print(a)
a.discard(50)
print(a)
a.discard(30)
print(a)
a.discard(50)
print(a)
a.discard(1000)
print(a)