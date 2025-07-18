class Account:
    __minbal=5000
    def __init__(self,a,cn,b):
        self.__accno=a
        self.__cname=cn
        self.__balance=b
    def deposite(self,t):
        self.__balance+=t
    def withdraw(self,t):
        if (self.__balance-t)<=Account.__minbal:
            print('Insuff Balance')
        else:
            self.__balance-=t
    def print_account(self):
        print(f'AccountNo: {self.__accno}')
        print(f'CustomerName: {self.__cname}')
        print(f'Balance: {self.__balance}')
    @classmethod
    def setminbal(cls,mb):
        cls.__minbal=mb

acc1=Account(101,'Naresh',50000)
acc1.print_account()
acc1.deposite(5000)
acc1.print_account()
acc1.withdraw(51000)
acc1.withdraw(45000)
acc1.print_account()
Account.setminbal(2000)
acc1.withdraw(9000)
acc1.withdraw(7999)
acc1.print_account()