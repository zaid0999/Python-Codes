# Python | Count the Number of matching characters in 
# a pair of string
# The problem is about finding how many characters are the same in two strings. We compare the strings and count the common characters between them


str1="java"
str2="javascript"
str3=""
for ch in str1:
    if ch not in str3:
        str3=str3+ch

c=0
for ch in str3:
    if ch in str2:
        c=c+1
print(c)