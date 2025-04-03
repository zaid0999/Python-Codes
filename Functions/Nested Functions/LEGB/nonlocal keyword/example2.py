def fun1():
    print("inside fun1")
    def fun2():
        print("inside fun2")
    return fun2
f2=fun1()
f2()