class A:
    def m1(self):
        print("Instance Method")
    @classmethod
    def m2(cls):
        print('Class Method')

A.m2()
obj1=A()
obj1.m1()
obj1.m2()