def fun1(a,b): # a,b are required arguments
    print(a,b)

def fun2(a=0,b=0): # a,b are default argument
    print(a,b)

def fun3(a,b=None): # a required, b default
    print(a,b)

'''
def fun4(b=None,a): # b default, a required
    print(a,b)
'''


fun1(10,20)
fun2()
fun2(1)
fun2(b=2)
fun3(6,9)
fun3(9)
# fun3(b=3)