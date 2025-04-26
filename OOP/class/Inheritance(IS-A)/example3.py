class A: # Parent Class
    def __init__(self):
        self.__x=100 # private variable
        self._y=200 # protected variable
        self.z=300 # public variable

class B(A): # Child class
    def m1(self):
        print("Protected y=",self._y)
        print("Public z=",self.z)
        # print("private x=",self.__x)

objb=B()
objb.m1()
print(objb.z)
# print(objb.__x)
# print(objb._y)