x=100
def fun1():
    global x
    x=200
    def fun2():
        global x
        x=300
    print(x)
    fun2()
print(x)
fun1()
print(x)