def factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    print(f'Factorial of {num} is {f}')

factorial(5) # Positional argument
factorial(num=11) # Keyword argument