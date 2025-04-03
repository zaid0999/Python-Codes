def calculate(n1,n2,calc):
    res=calc(n1,n2)
    return res

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def div(a,b):
    return a/b


res1=calculate(10,20,add)
res2=calculate(65,6,sub)
res3=calculate(3,88,multiply)
res4=calculate(90,9,div)
print(res1,res2,res3,res4)