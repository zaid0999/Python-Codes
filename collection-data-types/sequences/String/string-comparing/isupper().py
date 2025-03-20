# isupper(): This method returns True, if letters in string are in uppercase else False 

# str1="PYTHON"
# str2=str1.isupper()
# print(str2)


# print()


# str3="PYTHOn"
# str4=str3.isupper()
# print(str4)



# Write a program to verify string is in uppercase or not 
# without using isupper method 

str1=input("Enter any String ")
for ch in str1:
    if ch>='a' and ch<='z':
        print(False)
        break
else:
    print(True)