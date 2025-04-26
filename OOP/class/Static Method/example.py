class A:
    @staticmethod
    def m1():
        print("static method1")
    @staticmethod
    def m2(x):
        print("static method2")

A.m1()
A.m2(100)