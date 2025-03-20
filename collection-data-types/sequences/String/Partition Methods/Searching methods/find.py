# str.find(sub[, start[, end]]) 
# Return the lowest index in the string where substring sub is found within the slice s[start:end]



str1="python py jython java"
str2=str1.find("py")
print(str2)


print()


str3=str1.find("jy")
print(str3)


print()


str4=str1.find('jy',5,15)
print(str4)


print()


str5=str1.find('py',4)
print(str5)


print()


str6=str1.find("my")
print(str6)