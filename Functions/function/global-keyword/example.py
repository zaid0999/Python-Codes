x=100 # Global Variable
y=200 # Global Variable

def fun1():
    print(x,y)

def fun2():
    global x,y,p
    x=400
    y=500
    p=600 # Global Variable

fun1()
fun2()

print(x,y,p)