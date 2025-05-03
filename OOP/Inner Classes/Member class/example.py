class A:
    class __B:
        def m1(self):
            print("m1 method of B")
    def __init__(self):
        self.__b=A.__B()
    def m2(self):
        print("m2 method of A")
        self.__b.m1()

obja=A()
obja.m2()