# update(*others) 
# set |= other | ... 
# Update the set, adding elements from al others. 


s1={1,2,3}
s2={2,4,6}
s1 |= s2
print(s1)

A={1,2,3} 
B={4,5,6}
A.update(B)
print(A)