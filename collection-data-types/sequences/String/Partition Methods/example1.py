# Write a program to partition string without using 
# partition method 
# input 
# string : a,b,c,d,e 
# sep : , 
# output: ("a",",",b,c,d,e") 



str1="a,b,c,d,e"
sep=","
i=str1.find(sep)
left=str1[:i]
if i==-1:
    right=""
else:
    i=i+1
    right=str1[i:]

if sep not in str1:
    sep=""
t1=(left,sep,right)
print(t1)