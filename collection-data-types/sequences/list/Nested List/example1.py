# Write a program to print upper and lower triangle of matrix

A=[[10,20,30],[40,50,60],[70,80,90]] 

print("Upper Triangle")
for i in range(3):
    for j in range(3):
        if j>=i:
            print(A[i][j],end=' ')
        else:
            print("  ",end=" ")
    print()

print("Lower Triangle")
for i in range(3):
    for j in range(i+1):
        print(A[i][j],end=' ')
    print()