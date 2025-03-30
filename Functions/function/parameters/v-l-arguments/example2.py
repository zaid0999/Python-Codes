def mean(*a):
    s=0
    for value in a:
        s=s+value
    if len(a)!=0:
        m=s/len(a)
    else:
        m=0
    return m

x=[5,9,6,7,8,9]
res=mean(*x)
print(f'{x}{res:.2f}')
y=[]
res=mean(*y)
print(y,res)