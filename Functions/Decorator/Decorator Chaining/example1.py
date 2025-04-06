def upper(fun):
    def wrapper_fun(a):
        for s in a:
            print(s.upper())
    return wrapper_fun


@upper
def list_name(a):
    for s in a:
        print(s)


A=["zaid","shivi","isha","rohit"]
list_name(A)