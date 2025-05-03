class Matrix:
    def read_matrix(self,m,n):
        self.__rows=m
        self.__cols=n
        self.__a=[[int(input()) for j in range(n)] for i in range(m)]
    def print_matrix(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(self.__a[i][j],end=' ')
            print()
    def __add__(self,other):
        res=Matrix()
        res.__rows=self.__rows
        res.__cols=self.__cols
        res.__a=[[self.__a[i][j]+other.__a[i][j] for j in range(self.__cols)] for i in range(self.__rows)]
        return res

matrix1=Matrix()
matrix1.read_matrix(2,2)
matrix1.print_matrix()
matrix2=Matrix()
matrix2.read_matrix(2,2)
matrix2.print_matrix()
matrix3=matrix1+matrix2
matrix3.print_matrix()