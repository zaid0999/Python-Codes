def sort_list(a,*,ascending=True):
    if ascending:
        for i in range(len(a)):
            for j in range(len(a)-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
    else:
        for i in range(len(a)):
            for j in range(len(a)-1):
                if a[j]<a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
    
L1=[3,8,5,2,4,1,7]
print(f'Before Sorting {L1}')
sort_list(L1)
print(f'After Sorting {L1}')
sort_list(L1,ascending=False)
print(f'After Sorting{L1}')