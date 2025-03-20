# Write a program to print count of each character within string 
# input : aabbbaacccd 
# output : 4a3b3c1d 



str1="aabbaaccd"
str2=""
str3=""
for ch in str1:
    if ch not in str2:
        str2=str2+ch
print(str2)
for ch in str2:
    c=str1.count(ch)
    str3=str3+str(c)+ch
print(str3)
