# Write a function to find factorial of given number 
# using recursion 

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
n=int(input("Enter any number "))
res=factorial(n)
print(f'Factorial of {n} is {res}')