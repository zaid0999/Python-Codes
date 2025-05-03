class Person:
    class __Address:
        def __init__(self):
            self.__street=None
            self.__city=None
        def read_address(self):
            self.__street=input("Street: ")
            self.__city=input("City: ")
        def print_address(self):
            print(f'Street {self.__street}')
            print(f'City {self.__city}')
    def __init__(self):
        self.__name=None
        self.__add1=Person.__Address()
        self.__add2=Person.__Address()
    def read_person(self):
        self.__name=input("Name: ")
        self.__add1.read_address()
        self.__add2.read_address()
    def print_person(self):
        print(f'Name {self.__name}')
        self.__add1.print_address()
        self.__add2.print_address()

p1=Person()
p1.read_person()
p1.print_person()