def fun1():
    x=100 # Local Variable of fun1/non local variable of fun2
    def fun2():
        nonlocal x
        x=300
        print(x)
    fun2()
    print(x)
fun1()