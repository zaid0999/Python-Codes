# Applying multiple decorators to function is called decorator chaining 
# A decorator receives input as another decorator function. 


def draw_dollar(f):
    def wrapper_fun():
        print("$"*30)
        f()
        print("$"*30)
    return wrapper_fun


def draw_starts(f):
    def wrapper_fun():
        print("*"*30)
        f()
        print("*"*30)
    return wrapper_fun


@draw_dollar
@draw_starts
def display():
    print("PYTHON LANGUAGE")

display()