# str.ljust(width[, fillchar]) 
# Return the string left justified in a string of length width.


# str1="abc"
# str2=str1.ljust(10)
# print(len(str1))
# print(len(str2))
# print(str1)
# print(str2)

# print()

# str3=str1.ljust(10)
# str3=str1.ljust(10,"*")
# print(str3)



names=["naresh","ramu","kiran","ramesh","rajesh kumar"] 
for name in names:
    print(name.ljust(15,"*"))
    