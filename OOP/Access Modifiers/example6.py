class Matrix:
    def __init__(self,r,c):
        self.__m=[[0 for j in range(c)] for i in range(r)]
        self.__row=r
        self.__col=c
    
    def print_matrix(self):
        for i in range(self.__row):
            for j in range(self.__col):
                print(self.__m[i][j],end=' ')
            print()

    def set_value(self,row,col,value):
        self.__m[row][col]=value
    def get_value(self,row,col):
        return self.__m[row][col]
    
matrix1=Matrix(3,3)
matrix1.print_matrix()
matrix1.set_value(0,0,20)
matrix1.set_value(0,1,10)
matrix1.print_matrix()