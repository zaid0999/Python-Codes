A=[10,20,30,40,50,60,70,80,90,100] 
print(A)

B=A[0:3:1]
print(B)

C=A[-1:-4:-1]
print(C)

D=A[0:len(A):2]
print(D)

E=A[1:len(A):2]
print(E)

F=A[-1:-(len(A)+1):-2]
print(F)

G=A[-8:-10:2]
print(G)

G=A[8:0:-1]
print(G)

I=A[-1:-(len(A)+1):-1]
print(I)

str1="NARESH"
str2=str1[-1:-(len(str1)+1):-1]
print(str1,str2)