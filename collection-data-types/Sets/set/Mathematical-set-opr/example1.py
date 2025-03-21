# Find Common elements in three Lists using Sets – Python 


a = [1, 2, 3, 4] 
b = [2, 3, 5, 6] 
c = [1, 2, 3, 7] 
d=set(a)&set(b)&set(c)
print(a,b,c,d,sep="\n")