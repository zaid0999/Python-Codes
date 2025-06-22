class Product:
    def __init__(self):
        self.pname=None
        self.price=None
    def setProduct(self,pn,p):
        self.pname=pn
        self.price=p
    def getProduct(self):
        print(f'{self.pname},{self.price}')

p1=Product()
p1.setProduct("mouse",200)
p1.getProduct()
p2=Product()
p2.setProduct("Keyboard",800)
p2.getProduct()