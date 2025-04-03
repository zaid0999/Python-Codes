def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()


print("================================")




# Example:

def outer():
    x=100 # Local Variable of Outer Function
    y=200 # Local Variable of Outer Function
    def inner():
        print(x)
        print(y)
    inner()
    print(x)
    print(y)
outer()