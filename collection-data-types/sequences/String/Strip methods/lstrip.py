# str.lstrip([chars])
# Return a copy of the string with leading characters removed.The chars argument is a string specifying the set of characters to beremoved. If omitted or None, the chars argument defaults toremoving whitespace. The chars argument is not a prefix; rather, allcombinations of its values are stripped:






# str1="   nit"
# str2="nit"
# str3=str1==str2
# print(str3)

# str3=str1.lstrip()
# print(str3)
# str1=str3==str2
# print(str1)


# Example:

uname=input("UserName ")
if uname.strip()=="nit":
    print("Welcome")
else:
    print("Invalid Username")