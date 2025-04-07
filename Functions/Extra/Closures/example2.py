def calculator(n1,n2):
    def calculate(opr):
        match(opr):
            case'+':
                return n1+n2
            case'-':
                return n1-n2
            case'*':
                return n1*n2
            case'/':
                return n1/n2
    return calculate

calc1=calculator(5,2)
calc2=calculator(6,3)
res1=calc1('+')
res2=calc1('-')
res3=calc2('*')
res4=calc2('+')
res5=calc1('/')
print(res1,res2,res5)
print(res3,res4)