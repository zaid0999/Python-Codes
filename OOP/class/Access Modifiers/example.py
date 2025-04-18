class A:
    def __init__(self):
        self.__x=10 # private instance variable
        self.y=20 # public instace variable

obj1=A()
# print(obj1.__x)
print(obj1.y)