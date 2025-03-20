num=1
for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print(num,end=' ')
            num+=1
        else:
            print(' ',end=' ')
    print()  



