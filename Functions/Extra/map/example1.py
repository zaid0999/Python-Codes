A=[10,20,30,40,50]
B=[1,2,3,4,5]
C=list(map(lambda x,y:x+y,A,B))
D=list(map(lambda x,y:x*y,A,B))
print(A,B,C,D,sep='\n')