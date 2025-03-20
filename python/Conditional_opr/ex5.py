# Write a program to find input number is divisible with 3 and 5

num=int(input("Enter any number"))
result="Divisible"if num%3==0 and num%5==0 else "Not Divisible"
print(f'{num} is {result} with 3 and 5')