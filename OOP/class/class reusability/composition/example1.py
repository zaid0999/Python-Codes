class Address:
    def __init__(self):
        self.__street=None
        self.__city=None
    def read_address(self):
        self.__street=input("Street: ")
        self.__city=input("City: ")
    def print_address(self):
        print(f'Street {self.__street}')
        print(f'City {self.__city}')

class Person:
    def __init__(self):
        self.__name=None
        self.__add=Address()
    def read_person(self):
        self.__name=input("Name: ")
        self.__add.read_address()
    def print_person(self):
        print(f'Name {self.__name}')
        self.__add.print_address()

p1=Person()
p1.read_person()
p1.print_person()