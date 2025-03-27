# Iter() function 
# This function returns iterator object, which iterate each time one key from dictionary 
 
# iter(dictionary-name) 


grade_dict={'naresh':'A', 
            'suresh':'B', 
            'ramesh':'A', 
            'rajesh':'C', 
            'kishore':'A', 
            'kiran':'C'}
a=iter(grade_dict)
name1=next(a)
name2=next(a)
print(name1,name2)

print()

for name in a:
    print(name)

