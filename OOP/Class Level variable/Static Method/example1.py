class A:
    @staticmethod
    def m1():
        print("Statice Method")
    @staticmethod
    def m2(x):
        print(x)

A.m1()
A.m2(2)
A.m2('Zaid')