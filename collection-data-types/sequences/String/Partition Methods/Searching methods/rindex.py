# str.rindex(sub[, start[, end]]) 
# Like rfind() but raises ValueError when the substring sub is not found. 

str1="python java oracle python java"

str2=str1.rindex("java")
print(str2)


print()


str3=str1.index("java")
print(str3)


print()


# str4=str1.rindex("mysql")
# print(str4)