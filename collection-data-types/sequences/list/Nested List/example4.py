# Write a program to add two matrix with size of MxN

m=int(input("Enter how many rows? "))
n=int(input("Enter how many cols? "))

a=[]
b=[]
c=[]
print("Enter elements of a matris ")
for i in range(m):
    row=[]
    for j in range(n):
        value=int(input("Enter Value "))
        row.append(value)
    a.append(row)

print("Enter elements of b matrix ")
for i in range(m):
    row=[]
    for j in range(n):
        value=int(input("Enter Value "))
        row.append(value)
    b.append(row)

for i in range(m):
    row=[]
    for j in range(n):
        row.append(a[i][j]+b[i][j])
    c.append(row)
print(a,b,c,sep="\n")