x=100
y=200

def fun1():
    x=300
    y=400
    print(x,y)
    d=globals()
    print(d['x'],d['y']) # Global Variables
    d['x']=900
    d['y']=1000
    print(x,y)
    print(d['x'],d['y'])

fun1()
print(x,y)