# Return the string right justified in a string of length width.


str1="python"
str2=str1.rjust(10)
print(str2,len(str2))

str3=str1.rjust(10,'*')
print(str3)


# Example

students=[['naresh','python'],
          ['suresh','java'],
          ['ramesh','c++'],
          ['kishore','c']]

for stud in students:
    name=stud[0]
    course=stud[1]
    print(name.ljust(15,'*'),course.rjust(10,'#'))