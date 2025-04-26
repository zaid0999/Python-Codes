# Multilevel inheritance 

# If a class is derived from another derived class, it is called multilevel inheritance 


class A:
    def m1(self):
        print("m1 of A")

class B(A):
    def m2(self):
        print("m2 of B")

class C(B):
    def m3(self):
        print("m3 of C")

objc=C()
objc.m1()
objc.m2()
objc.m3()