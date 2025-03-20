spaces=4
k=102
for i in range(101,96,-1):
    for s in range(spaces):
        print(" ",end="")
    for j in range(101,i-1,-1):
        print(chr(j),end='')
    for l in range(k,102):
        print(chr(l),end='')
    k=k-1
    print()
    spaces=spaces-1