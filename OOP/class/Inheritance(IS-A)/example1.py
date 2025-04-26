class A: # parent class/base class/super class
    def __init__(self):
        self.x=100
        self.y=200

class B(A): # child class/derived class/sub class
    pass

objb=B()
print(objb.x,objb.y)