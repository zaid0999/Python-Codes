# str.rfind(sub[, start[, end]]) 
# Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure. 



str1="python java oracle python java"
str2=str1.find("java")
print(str2)


print()


str3=str1.rfind("java")
print(str3)


print()


str4=str1.find("mysql")
print(str4)


print()


str5=str1.rfind("mysql")
print(str5)