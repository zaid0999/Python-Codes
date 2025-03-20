# str.strip([chars]) 
# Return a copy of the string with the leading and trailing characters removed.


str1="  nit   "
str2=str1.strip()
print(str2,len(str2))


print()


str3="*****python*****"
str4=str3.strip("*")
print(str4)

print()

str5="@#$@#!zaid@#$%$#"
str6=str5.strip("@#$%!")
print(str6)

print()


str7="www.nareshit.com"
str8=str7.strip("wcom.")
print(str8)