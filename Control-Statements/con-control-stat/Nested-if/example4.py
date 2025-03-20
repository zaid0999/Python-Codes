# Write a program to check if the input number is even or odd  
# using nested if.

num=int(input("Enter any number "))
if num%2==0:
    print("Given number is Even")
else:
    if num%2!=0:
        print("Given number is Odd")