# title() : This method returns every word of string first letter in capital and remaining al letters in lowercase 
# Syntax: variable-name=string.title() 


# str1="python is programming langauge"
# str2=str1.title()
# print(str1)
# print(str2)

# print()


# str3="PYTHON IS PROGRAMMING LANGAUGE"
# str4=str3.title()
# print(str3)
# print(str4)





# convert input string into titlecase without using 
# predefined method (title) 

str1=input("Enter Any String ")
i=0
str2=""
while i<len(str1):
    if i==0:
        if str1[i]>='a' and str1[i]<='z':
            str2=str2+chr(ord(str1[i])-32)
        else:
            str2=str2+str1[i]
    elif str1[i]==' ':
        str2=str2+" "
        i=i+1
        if str1[i]>='a' and str1[i]<='z':
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

