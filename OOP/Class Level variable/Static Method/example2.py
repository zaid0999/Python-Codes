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

p1=Math.isprime(7)
print(p1)
p2=Math.isprime(8)
print(p2)

print("===========")

f1=Math.factorial(7)
print(f1)