class C:
    def __init__(self):
        self.__x=100 # private instance variable
        self.__y=200 # private instancd variable
    def print_xy(self): # public instance method
        print(f'{self.__x},{self.__y}')
    def setX(self,n):
        self.__x=n
    def setY(self,m):
        self.__y=m

obj1=C()
obj1.print_xy()
obj1.setX(10)
obj1.setY(20)
obj1.print_xy()