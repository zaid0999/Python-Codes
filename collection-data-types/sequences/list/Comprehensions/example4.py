# Adding two matrices using list comprehension (2x2) 

print("input elements of first matrix ")
matrix1=[[int(input()) for j in range(2)] for i in range(2)]
print("input elements of second matrix ")
matrix2=[[int(input()) for j in range(2)] for i in range(2)]

matrix3=[[matrix1 [i][j]+matrix2[i][j] for j in range(2)] for i in range(2)]

print(matrix1)
print(matrix2)
print(matrix3)