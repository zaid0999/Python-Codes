# get() method 
# Syntax: dictionary-name.get(key,default=None) 
# This method return value of given key, if key exists 
# If key not exists, it returns default value which is default to None 
# If default is given, it returns that value 
# This method never raises Keyerror 



d1={1:10,2:20,3:30,4:40,5:50}

value1=d1.get(1)
print(value1)

value2=d1.get(2)
print(value2)

value3=d1.get(5)
print(value3)

value4=d1.get(7)
print(value4)

value5=d1.get(8,80)
print(value5)

print(d1)