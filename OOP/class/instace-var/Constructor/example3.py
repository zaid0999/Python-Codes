class Product:
    def __init__(self):
        self.pname=None
        self.price=None
    def setProduct(self,pn,p):
        self.pname=pn
        self.price=p
    def printProduct(self):
        print(f'{self.pname},{self.price}')

p1=Product()
p1.setProduct("Mouse",200)
p2=Product()
p2.setProduct("Keyboard",1500)
p1.printProduct()
p2.printProduct()