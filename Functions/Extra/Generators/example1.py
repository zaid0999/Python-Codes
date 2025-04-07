# Generator Function
def backward_iterator(seq):
    for value in seq[::-1]:
        yield value

a=[10,20,30,40,50]
x=backward_iterator(a)
n1=next(x)
n2=next(x)
n3=next(x)
n4=next(x)
n5=next(x)
print(n1,n2,n3,n4,n5)

b=list(range(10,110,10))
y=backward_iterator(b)
for value in y:
    print(value,end=" ")