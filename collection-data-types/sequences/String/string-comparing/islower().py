# islower(): This method returns True, if string contain al lowercase letters else False.

# str1="python"
# str2=str1.islower()
# print(str2)

# print()

# str3="pythOn"
# str4=str3.islower()
# print(str4)



str1=input("Enter any String ")
for ch in str1:
    if ch>='A' and ch<='Z':
        print(False)
        break
else:
    print(True)