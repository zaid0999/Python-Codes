# When more than one subclass having similar role with different implementation that method is declared as abstract. 

import abc
class Shape(abc.ABC):
    def __init__(self):
        self._dim1=None
        self._dim2=None
    def read(self):
        self._dim1=float(input("Dim1: "))
        self._dim2=float(input("Dim2: "))
    @abc.abstractmethod
    def find_area(self):
        pass

class Triangle(Shape): #Concrete class
    def find_area(self):
        area=self._dim1*self._dim2*0.5
        return area

class Rectangle(Shape): # Concrete class
    def find_area(self):
        area=self._dim1*self._dim2
        return area
    
t1=Triangle()
t1.read()
print(f'Area of triange is {t1.find_area()}')
r1=Rectangle()
r1.read()
print(f'Area of Rectangle is {r1.find_area()}')