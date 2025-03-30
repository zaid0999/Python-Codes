def findmax(**a):
    m=0
    for key,value in a.items():
        if m==0:
            m=value
            t=(key,value)
        elif m<value:
            m=value
            t=(key,value)
    return t

res=findmax(a=20,b=60,c=70)
print(res)
res=findmax(sub1=75,sub2=65,sub3=88)
print(res)

# Variable length keyword only arguments are used to manipulate dictionary data 