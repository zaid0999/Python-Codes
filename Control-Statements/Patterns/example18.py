spaces=4
for i in range(1,6):
    for s in range(spaces):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    spaces=spaces-1

print()

spaces=0
for i in range(5,0,-1):
    for s in range(spaces):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    spaces=spaces+1