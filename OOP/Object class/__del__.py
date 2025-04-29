# This method is executed automatically before object is deleted by garbage collector. A block of code which has to be executed before deleting object is written inside destructor. Resource alocation is done within constructor and resource de-alocation is done within destructor. 

class A:
    def __init__(self): # Overriding method
        print("inside __init__ method")
    def __del__(self): # Overriding method
        print("inside __del__ method")

obja=A()
del obja