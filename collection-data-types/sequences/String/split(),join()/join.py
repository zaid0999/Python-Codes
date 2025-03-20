# join() method 
# This method joins colection of string into one string using separator 

# Syntax: separator.join(iterable) 

# Iterable or colection which contains more than one string 


s1="a,b,c,d,e"
a=s1.split(",")
print(a)
s2=",".join(a)
print(s2)