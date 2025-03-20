# Write  a program to find given string within string 
# search from right to left and return last index 
# without using rfind method 




str1="java python java oracle"
search="java"
i=-1
start=-len(search)
while i>-len(str1):
    if i==-1:
        s=str1[-len(search):]
        if s==search:
            print(len(str1)-(search))
            break
    else:
        s=str1[start-1:i]
        if s==search:
            print(len(str1)-1+start)
            break
    i=i-1
    start=start-1
if i==-len(str1):
    print(-1)