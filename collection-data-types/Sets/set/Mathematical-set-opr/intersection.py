# intersection(*others) 
# set & other & ... 
# Return a new set with elements common to the set and al others. 

a={1,2,3,4,5}
b={1,2,3,6,7}
c=b.intersection(a)
print(c)


print("===============")

python_students={'naresh','ramesh','kishore','rajesh'} 
java_students={'ramesh','kiran','raman','naresh'} 

print(python_students)
print(java_students)
python_java_students=python_students&java_students
print(python_java_students)


print("=============================")
a=[1,2,3]
b={1,2,4}
print(b.intersection(a))
