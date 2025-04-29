import abc
class Animal(abc.ABC): # Abstract Base Class
    @abc.abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def eat(self): # Overriding Method
        print("Dog Eat...")

class Cat(Animal):
    def eat(self): # Overriding method
        print("Cat Eat...")

class Cow(Animal):
    def eat(self): # Overriding method
        print("Cow Eat...")

d1=Dog()
c1=Cat()
d1.eat()
c1.eat()
c2=Cow()
c2.eat()