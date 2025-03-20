# str.center(width[, fillchar])
# Return centered in a string of length width. Padding is doneusing the specified fillchar (default is an ASCII space). Theoriginal string is returned if width is less than or equal to len(s).



# str1="zaid"
# str2=str1.center(10,"*")
# print(str2)


# print()


# str3="c++"
# str4=str3.center(10,'*')
# print(str4)


# Example:



names=["naresh","suresh","ramesh","kiran","ramu"]

for name in names:
    print(name.center(15,'#'))