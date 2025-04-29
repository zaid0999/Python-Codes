class Amithab:
    def act(self): # Overriden Method
        print("Very Good Acting")

class Abhishek(Amithab):
    def act(self): # Overriding Method
        print("Bad in Acting")

c1=Abhishek()
c1.act()