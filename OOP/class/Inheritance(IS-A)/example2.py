class A:
    def __init__(self):
        self.x=100
        self.y=200

class B(A):
    def __init__(self):
        super().__init__()
        self.p=300
        self.q=400

objb=B()
print(objb.x,objb.y)
print(objb.p,objb.q)


# It is required to call the constructor of base class within derived class, to inherit properties of base class inside derived class