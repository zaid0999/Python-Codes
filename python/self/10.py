# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end=' ')
#     print()

print()

for i in range(5,0,-1):
    for j in range(i,6):
        print('*',end=' ')
    print()

print()

for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

print()

for i in range(5,0,-1):
    for j in range(1,6):
        if i>=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()