class A:
    x=100
    def __init__(self):
        self.y=200

print(A.x)
obj1=A()
print(obj1.y)
obj2=A()
print(obj2.y)
obj3=A()
print(obj3.y)
print(obj1.x)
print(obj2.x)
print(obj3.x)
A.x=300
print(obj1.x)