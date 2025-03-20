# Write a program to create 3x3 matrix and display

a=[]
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("Enter any value "))
        row.append(value)
    a.append(row)

for row in a:
    for col in row:
        print(col,end=' ')
    print()