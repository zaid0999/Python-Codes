class B:
    def m1(self):
        print("public method")
    def __m2(self):
        print("private method")

obj1=B()
obj1.m1()
# obj1.__m2()