# If a class derived from more than one base class it is called multiple inheritance.

class A: #Base Class/Super Class
    def m1(self):
        print("m1 method of class A")

class B: # Base Class/Super Class
    def m2(self):
        print("m2 method of class B")

class C(A,B): # Derived Class/Sub Class
    def m3(self):
        print("m3 method of class C")

objc=C()
objc.m1()
objc.m2()
objc.m3()