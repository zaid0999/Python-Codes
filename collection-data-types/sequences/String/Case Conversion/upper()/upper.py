# upper() : This convert string into uppercase 
# <variable-name>=string.upper()



str1="python"
str2=str1.upper()
print(str1)
print(str2)


# Write a program to convert input string into uppercase 
# without using upper() method 


str1=input("Enter any string ")
str2=""
for ch in str1:
    if ch>='a' and ch<='z':
        str2=str2+chr(ord(ch)-32)
    else:
        str2=str2+ch
print(str1,str2,sep="\n")