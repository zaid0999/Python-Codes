A=[10,20,30,40,50]
print(A[0],A[1],A[2],A[3],A[4])

print(A[-1],A[-2],A[-3],A[-4],A[-5])


print()


B=list(range(10,110,10))
print(B)
print(len(B))

print()

print("Reading Data in Forward Direction")
for i in range(len(B)):
    print(B[i],end=' ')


print()

print("\nReading Data in Backward Direction")
for i in range(-1,-(len(B)+1),-1):
    print(B[i],end=' ')