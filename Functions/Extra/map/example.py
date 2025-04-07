A=[10,20,30,40,50]
B=list(map(lambda value:str(value),A))
print(A)
print(B)

C=list(map(lambda value:int(value),B))
print(C)

x, y, z = list(map(lambda value: int(value), input().split()))
print(x,y,z)

D=['naresh','ramesh','suresh','kishore']
E=list(map(lambda s:s.upper(),D))
print(D,E,sep='\n')