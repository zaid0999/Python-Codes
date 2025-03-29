# A function can access global variable directly but cannot modify or update global variable directly 

x=100 # Global Variable
y=200 # Global Variable

def fun1():
    print(x,y)
    
def fun2():
    x=300 # Local Variable
    y=400 # Local Variable
    x=500
    p=600 # Local Variable
    print(x,y,p)

fun1()
fun2()
fun1()