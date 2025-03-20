# Python – Convert Pascal case to Snake case 
 
# StudentName 
# student_name


str1="PythonProgrammingLanguage"
str2=''

for i in range(len(str1)):
    if i==0:
        str2=str2+str1[i].lower()
    elif str1 [i].isupper():
        str2=str2+"_"+str1 [i].lower()
    else:
        str2=str2+str1[i].lower()
print(str1)
print(str2)