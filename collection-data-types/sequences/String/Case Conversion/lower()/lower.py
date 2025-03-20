# lower() : This method returns string in lowercase 
# Syntax: <variable-name>=string.lower() 


str1="PYTHON"
str2=str1.lower()
print(str1,str2,sep="\n")



# Write a program to convert input string into lowercase 
# without using lower() method 

str1=input("Enter any String ")
str2=""
for ch in str1:
    if ch>='A' and ch<='Z':
        str2=str2+chr(ord(ch)+32)
    else:
        str2=str2+ch
print(str1,str2,sep='\n')