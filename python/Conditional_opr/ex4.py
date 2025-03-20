# Write a program to find input number is 3 digit number or not

num=int(input("Enter any integer number"))
result="3 Digit Number"if num>=100 and num<=999 else "Not 3 Digit Number"
print(result)