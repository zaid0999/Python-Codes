# Type hints, introduced in Python 3.5 as a part of the standard library via PEP 484, alow you to specify the expected type of a variable, function parameter, or return value.





a:int=10
b:int=1.5
print(a)
print(b)


print()


# Example

def add(n1:int,n2:int)->int:
    n3=n1+n2
    return n3

res1=add(20,10)
res2=add(40,50)
print(res1,res2)
res3=add(5.5,6.3)
print(res3)