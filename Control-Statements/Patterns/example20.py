spaces=4
for i in range(97,102):
    for s in range(spaces):
        print(" ",end="")
    for j in range(97,i+1):
        if j==97 or j==i:
            print("a",end=' ')
        else:
            print(chr(j),end=' ')
    print()
    spaces=spaces-1