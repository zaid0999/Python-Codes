class A: # parent class or base class
    def m1(self):
        print("m1 method of base class")
    def m2(self):
        print("m2 method of base class")

class B(A): # child class or derived class
    def m3(self):
        print("m3 method of derived class")

objb=B()
objb.m1()
objb.m2()
objb.m3()