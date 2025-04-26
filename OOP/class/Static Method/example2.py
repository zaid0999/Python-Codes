class Math:
    @staticmethod
    def isprime(num):
        c=0
        for i in range(1,num+1):
            if num%i==0:
                c=c+1
        return c==2
    @staticmethod
    def factorial(num):
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        return fact

b1=Math.isprime(5)
b2=Math.factorial(4)
print(b1)
print(b2)