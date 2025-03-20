# Python | Multiply Adjacent elements 
# The original tuple : (1, 5, 7, 8, 10) 
# Resultant tuple after multiplication : (5, 35, 56, 80) 


t1=(1,5,7,8,10)
a=[]
for i in range(len(t1)-1):
    a.append(t1[i]*t1[i+1])
a=tuple(a)
print(a)
