# This method returns True if String contains 
# 1. only alphabets 
# 2. only digits 
# 3. alphabets and digits 
# else return False 


# str1="abc"
# str2=str1.isalnum()
# print(str2)

# print()

# str3="1234567890"
# str4=str3.isalnum()
# print(str4)

# print()

# str5="za3id123"
# str6=str5.isalnum()
# print(str6)

# print()

# str7="abc#"
# str8=str7.isalnum()
# print(str8)



str1=input("Enter any String ")
for ch in str1:
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z') or (ch>='0' and ch<='9'):
        pass
    else:
        print(False)
        break
else:
    print(True)