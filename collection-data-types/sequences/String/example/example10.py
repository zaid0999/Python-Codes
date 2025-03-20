# Python – Convert Pascal case to Snake case 
# StudentName 
# student_name


str1="PythonProgrammingLanguage"
a=[]
i=0
str2=''
while i<len(str1)-1:
    if str1[i+1].isupper():
        a.append(str2+str1[i])
        str2=''
        str2=str2+str1[i+1]
        i=i+1
    else:
        str2=str2+str1[i]
    i=i+1
a.append(str2+str1[-1])
b=[s.lower() for s in a]
str3='_'.join(b)
print(str1)
print(str3)