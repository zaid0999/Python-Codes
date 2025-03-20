# str.rstrip([chars])
# Return a copy of the string with trailing characters removed.The chars argument is a string specifying the set of characters to beremoved. If omitted or None, the chars argument defaults toremoving whitespace. The chars argument is not a suffix; rather, allcombinations of its values are stripped:








str1="zaid      "
str2=str1.rstrip()
print(str1,len(str1))
print(str2,len(str2))


print()


str3="zaid*******"
str4=str3.rstrip("*")
print(str4)

print()


str5="zaid@#$#$#@#$#$@"
str6=str5.rstrip("@#$")
print(str6)