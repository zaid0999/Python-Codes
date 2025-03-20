# Write a program to delete leading and trailing 
# characters from string without using strip method 
 
# input 
# string --> ***python*** 
# char --> * 
# output --> python 


str1=input("Enter any String ")
char=input("Character to Remove ")
i=0
while i<len(str1):
    if str1 [i] in char:
        i=i+1
    else:
        break
str1=str1[i:]

i=-1
while i>=-(len(str1)):
    if str1 [i] in char:
        i=i-1
    else:
        break
str1=str1[:i+1]
print(str1)