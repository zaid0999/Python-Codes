# __new__()  
# Always object is created by invoking __new__ method. 
# This __new__ method invokes constructor of class. 
# This method is override in order to restrict object creation. 


class Alpha:

    def __new__(cls,*vargs,**kwargs): # Overriding method
        print("Inside New Method")
        print(vargs)
        obj=super().__new__(cls)
        return obj
    def __init__(self,x,y):
        print("inside constructor")
        print(x,y)

a1=Alpha(10,20)