# Syntax2: import module-name as <alias-name> 
# Importing module inside current module with another name 



def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
    
def isPrime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
    return c==2

def isamstrong(num):
    num1=num
    s=0
    while num>0:
        d=num%10
        s=s+(d**3)
        num=num//10
    return s==num1
