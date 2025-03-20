# Write a program to remove string with trailing characters
# string without using rstrip
# input
# string : nit****
# char : *
# output : nit





str1=input("Enter Any String ")
char=input("Enter Character to remove ")

i=-1
while i>=-(len(str1)):
    if str1 [i] in char:
        i=i-1
    else:
        break
str2=str1[:i+1]
print(str1)
print(str2)