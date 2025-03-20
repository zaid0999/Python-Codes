spaces=0
k=4
for i in range(5,0,-1):
    for s in range(spaces):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end='')
    for l in range(k,0,-1):
        print(l,end='')
    spaces=spaces+1
    print()
    k=k-1