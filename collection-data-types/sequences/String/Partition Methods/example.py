# Write a program to partition string without using 
# partition method 
# input 
# string : a,b,c,d,e 
# sep : , 
# output: ("a",",",b,c,d,e")




str1="a,b,c,d,e"
sep=","
i=0
left=''

while i<len(str1):
    if str1 [i]!=sep:
        left=left+str1[i]
    else:
        break
    i=i+1

i=i+1
right=str1[i:]
if sep not in str1:
    sep=""
t1=(left,sep,right)
print(t1)