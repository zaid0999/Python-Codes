# isdigit() 
# This method return True, if string contains only digits else False


# str1="123654"
# str2=str1.isdigit()
# print(str2)

# print()

# str3="a1365"
# str4=str3.isdigit()
# print(str4)




# Write a program to print sum of two numbers 
# input two numbers from keyboard


# n1=input("Enter First Number ")
# n2=input("Enter Second Number ")
# if n1.isdigit() and n2.isdigit():
#     n1=int(n1)
#     n2=int(n2)
#     n3=n1+n2
#     print(f'sum of {n1} and {n2} is {n3}')
# else:
#     print("input values must be integer type")



# Write a program to find string contains only digits 
# or not without using isdigit method 

str1=input("Enter any String ")
for ch in str1:
    if ch>='0' and ch<='9':
        continue
    else:
        print(False)
        break
else:
    print(True)