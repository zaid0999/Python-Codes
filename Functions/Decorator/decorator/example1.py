def authentication(fun):
    def wrapper_fun():
        user=input("UserName: ")
        psd=input("Password: ")
        if user=="zaid" and psd=="zaid0444":
            fun()
        else:
            print("authentication fail")
    return wrapper_fun

@authentication
def withdraw():
    print("whithraw function")


def deposit():
    print("deposit function")


withdraw()
deposit()