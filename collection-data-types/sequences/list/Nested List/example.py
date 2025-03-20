A=[[10,20,30],[40,50,60],[70,80,90]] 

# Read elements from matrix using index

for i in range(3):
    for j in range(3):
        print(A[i][j],end=" ")
    print()


# Read elements from matrix using for loop 

for row in A:
    for col in row:
        print(col,end=' ')
    print()