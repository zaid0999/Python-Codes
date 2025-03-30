# Sort function (Bubble Sorting) 


def sorList(a:list):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

L1=[2,7,3,5,1,4,6]
print(f'Before Sorting {L1}')
sorList(L1)
print(f'After Sorting {L1}')