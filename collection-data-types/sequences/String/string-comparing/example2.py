# Python – Avoid Spaces in string length 
# When working with strings in Python, 
# we may sometimes need to calculate the length of a string 
# excluding spaces. 


str1=input("Enter any String ")
s=0
for ch in str1:
    if ch!=' ':
        s+=1
print(f'length of string without spaces {s}')