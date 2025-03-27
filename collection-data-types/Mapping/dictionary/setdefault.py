# setdefault(key,default=None) 

# This method performs two operations 
# 1. Reading value of given key, if key exists 
# 2. If not exists, this method add key and value within dictionary. It 
#     will add key with default value which default to None 



d1={1:10,2:20,3:30}
value1=d1.setdefault(1)
print(value1)

value2=d1.setdefault(3)
print(value2)

value3=d1.setdefault(5)
print(value3)
print(d1)

value4=d1.setdefault(4,40)
print(value4)
print(d1)