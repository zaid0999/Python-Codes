# input : 4a3b3c1d 
# output : aaaabbbcccd 



str1="4a3b3c1d"
i=0
str2=""
while i<len(str1):
    n=int(str1[i])
    char=str1[i+1]
    str2=str2+(n*char)
    i=i+2
    
print(str1)
print(str2)