x=100 # Global Variable
def outer():
    y=200 # Local variable of outer function
    def inner():
        z=300 # Local Variable of inner function
        print(x)
        print(y)
        print(z)
        print(__name__) # Builtins
        # print(p) Error
    inner()
outer()



