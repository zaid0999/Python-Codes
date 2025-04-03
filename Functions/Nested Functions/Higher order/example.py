def fun1(f):
    f()

def fun2():
    print("fun2")
def fun3():
    print("fun3")
def fun4():
    print("fun4")

fun1(fun2)
fun1(fun3)
fun1(fun4)