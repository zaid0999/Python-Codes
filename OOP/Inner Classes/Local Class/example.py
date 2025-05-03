class A:
    def m1(self):
        class B: #Local Class
            def m2(self):
                print("m2 of B class")
        objb=B()
        objb.m2()
        print("m1 of A Class")

objb=A()
objb.m1()