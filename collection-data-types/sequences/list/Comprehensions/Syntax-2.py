A=[3,7,9,1,2,5,4,12,23,57,89,33,65,97,42] 
B=[value for value in A if value%2==0]
C=[value for value in A if value%2!=0]
print(A,B,C,sep="\n")