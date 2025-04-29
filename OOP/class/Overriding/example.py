class Parent:
    def eat(self): # Overriden Method
        print("Eat Veg")

class Child(Parent):
    def eat(self): # Overrriding Method
        print("Eat Non Veg")
    def sleep(self):
        print("Sleep")

c1=Child()
c1.eat()
c1.sleep() 