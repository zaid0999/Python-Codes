# Write a program to capitalize string without 
#using capitalize() method 

str1=input("Enter any String ")
str2=""
i=0
while i<len(str1):
    if i==0:
        if str1[i]>'a'and str1[i]<='z':
            str2=str2+chr(ord(str1[i])-32)
        else:
            str2=str2+str1[i]
    elif str1[i]>='A' and str1[i]<='Z':
        str2=str2+chr(ord(str1[i])+32)
    else:
        str2=str2+str1[i]
    i=i+1

print(str1)
print(str2)