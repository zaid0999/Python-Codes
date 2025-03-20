# A=[chr(num) for num in range(65,91)]
# B=[chr(num) for num in range(97,123)]
# print(A)
# print(B)


A=[1,2,3,4,5]
B=[6,7,8,9,10]
C=[A[i]+B[i] for i in range(5)]
print(A,B,C,sep="\n")