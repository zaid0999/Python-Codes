# Write a program to generate prime numbers from 3 to 50
for num in range(3,51):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c+=1
    if c==2:
        print(f'{num} is prime')