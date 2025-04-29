# Create a class which allows to create only one object 

class Product:
    count=0
    def __new__(cls,*vargs,**kwargs): # Overriding method
        if Product.count==0:
            p=super().__new__(cls)
            Product.count+=1
            return p
        else:
            return None
    def __init__(self):
        self.pname=None
        self.price=None

p1=Product()
print(p1)
p2=Product()
print(p2)
print(p1.pname,p1.price)