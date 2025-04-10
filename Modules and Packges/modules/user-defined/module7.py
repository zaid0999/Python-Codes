def fun1():
    print("fun1 of module7")

def fun2():
    print("fun2 of module7")

def fun3():
    print("fun3 of module7")

print(__name__)
if __name__=='__main__':
    fun1()
    fun2()
    fun3()