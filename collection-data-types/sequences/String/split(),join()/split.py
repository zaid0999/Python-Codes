# split() method is used to split the string into number of sub strings 
# using separator. The default separator used by split is space 

# string.split(sep=” “) 
             
# This method return list containing al the string. 




str1="python java oracle mysql"
a=str1.split()
print(a)

str2="python,java,oracle,mysql"
b=str2.split(",")

str3="a,b,c,d,e"
c=str3.split(",")
print(c)

str4="ab,ce,e"
d=str4.split(",")
print(d)