# Write  a program to find given string within string 
# search from left to right and return first index 
# without using find method 

str1="python java oracle java"
search="oracle"
i=0

while i<len(str1):
    word=str1[i:i+len(search)]
    if word==search:
        print(i)
        break
    i=i+1
if i==len(str1):
    print(-1)