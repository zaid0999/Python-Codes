# difference(*others) 
# set - other - ... 
# Return a new set with elements in the set that are not in the others. 



a={10,20,30,40,50}
b={10,20,30,50,60}
c=a.difference(b)
print(c)
d=b.difference(a)
print(d)



print("===================================")



python_students={'naresh','ramesh','kishore','rajesh'} 
java_students={'ramesh','kiran','raman','naresh'}

only_python=python_students-java_students
print(only_python)

only_java=java_students-python_students
print(only_java)