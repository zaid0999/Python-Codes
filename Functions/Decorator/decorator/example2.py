def smart_div(fun):
    def wrapper_fun(n1,n2):
        if n2==0:
            return 0
        else:
            return fun(n1,n2)
    return wrapper_fun

@smart_div
def div(n1,n2):
    n3=n1/n2
    return n3

x=int(input("Enter Value of X: "))
y=int(input("Enter Value of Y: "))
z=div(x,y)
print(f'{x}/{y}==>{z}')