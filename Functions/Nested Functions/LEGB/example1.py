# Inner function can access local variable of outer function but cannot modify or update directly. 


# example:

def fun1():
    x=100 # Local Variable of fun1
    def fun2():
        print(x)
    fun2()
    def fun3():
        x=400 # Create Local Variable in fun3
        print(x)
    fun3()
    print(x)
fun1()