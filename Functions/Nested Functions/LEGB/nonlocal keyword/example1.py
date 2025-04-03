def calculator(n1,n2,opr):
    res=None # Local Variable
    def add():
        nonlocal res
        res=n1+n2
    def sub():
        nonlocal res
        res=n1-n2
    def multiply():
        nonlocal res
        res=n1*n2
    def div():
        nonlocal res
        res=n1/n2
    match(opr):
        case '+':
            add()
        case '-':
            sub()
        case '*':
            multiply()
        case '/':
            div()
    return res
n1=int(input("First Number "))
n2=int(input("Second Number "))
opr=input("Enter Operator ")
result=calculator(n1,n2,opr)
print(f'{n1}{opr}{n2}={result}')