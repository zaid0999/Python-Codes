# str.expandtabs(tabsize=8) 
# Return a copy of the string where al tab characters are replaced by one or more spaces, depending on the current column and the given tab size. Tab positions occur every tabsize characters (default is 8, giving tab positions at columns 0, 8, 16 and so on).



str1="empno\tename\tsalary"
str2=str1.expandtabs()
print(str2)

print()

str3=str1.expandtabs(12)
print(str3)

print()

str4=str1.expandtabs(15)
print(str4)