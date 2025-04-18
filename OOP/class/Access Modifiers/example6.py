class Account:
    def __init__(self,a,cn,b):
        self.__accno=a
        self.__cname=cn
        self.__balance=b
    def deposite(self,t):
        self.__balance+=t
    def withdraw(self,t):
        if self.__balance<t:
            print("Insuff balance")
        else:
            self.__balance-=t
    def print_balance(self):
        print(f'Balance is {self.__balance}')

acc1=Account(101,"Zaid",80000)
acc1.print_balance()
acc1.deposite(20000)
acc1.print_balance()
acc1.withdraw(60000)
acc1.print_balance()