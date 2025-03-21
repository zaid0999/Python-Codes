# symmetric_difference(other) 
# set ^ other 
# Return a new set with elements in either the set or other but not both. 

a={1,2,3,4,5}
b={1,2,3,6,7}
c=a.symmetric_difference(b)
print(a,b,c,sep="\n")

d=a^b
print(d)