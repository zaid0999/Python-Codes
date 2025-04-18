class A:
    x=100 # Class Level Variable
    def __init__(self):
        self.y=200 # Instance Variable
    def m1(self):
        print(self.y)
        print(A.x)
    @classmethod
    def m2(cls):
        print(cls.x)
A.m2()
obj1=A()
obj1.m1()