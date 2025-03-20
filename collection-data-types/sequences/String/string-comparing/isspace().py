# isspace() 
# This method returns True, if string contains only spaces else False


# str1="    "
# str2=str1.isspace()
# print(str2)

# print()

# str3="  ab cd ef"
# str4=str3.isspace()
# print(str4)

# print()

# str5=""
# str6=str5.isspace()
# print(str6)



# Example: 
# Login


# user=input("UserName: ")
# if user.isspace() or not bool(user):
#     print("Username must contains alphabets")
# else:
#     print("Valid UserName")




# Write a program to find input string contains 
# only spaces without using isspace() method 


str1=input("Enter Any String ")
for ch in str1:
    if ch!=' ':
        print(False)
        break
else:
    print(True)