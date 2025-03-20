# Write a program to remove leading characters from
# string without using lstrip
# input
# string : ****nit
# char : *
# output : nit







str1=input("Enter Any String ")
char=input("Enter Character to remove ")

i=0
while i<len(str1):
    if str1 [i] in char:
        i+=1
    else:
        break
str2=str1[i:]
print(str1)
print(str2)