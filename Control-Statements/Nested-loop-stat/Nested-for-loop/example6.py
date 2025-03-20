# Write a program to generate factorial of all the numbers from 1 to 6

for num in range(1,7):
    fact=1
    for i in range(1,num+1):
     fact=fact*i
    print(f'{num}==>{fact}')