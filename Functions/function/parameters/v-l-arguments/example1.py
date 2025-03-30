def median(*a):
    if len(a)%2!=0:
        i=len(a)//2
        m=a[i]
    else:
        i=len(a)//2
        m=(a[i]+a[i-1])/2
    return m

a=[5,5,76,4,5,5,4]
res=median(*a)
print(res)
b=[10,20,30,40]
res=median(*b)
print(res)