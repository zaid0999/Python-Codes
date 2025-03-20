# isalpha(): This method returns True, if al letters within string are alphabets else False. 


# name="ZAID"
# name1=name.isalpha()
# print(name1)

# print()

# name3="zaid"
# name4=name3.isalpha()
# print(name4)

# print()

# name5='zaid123'
# name6=name5.isalpha()
# print(name6)

# print()

# name7='zaid#'
# name8=name7.isalpha()
# print(name8)


# Write a program to find input string is alphabetic 
# string or not without using isalpha method


str1=input("Enter Any String ")
for ch in str1:
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        pass
    else:
        print(False)
        break
else:
    print(True)