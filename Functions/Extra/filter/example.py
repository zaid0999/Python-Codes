# Filtering Even and Odd Numbers

A=[1,8,3,7,11,9,12,14,16,26,98,44,64,24,22]
B=list(filter(lambda num:num%2==0,A))
print(A)
print(B)
C=list(filter(lambda num:num%2!=0,A))
print(C)