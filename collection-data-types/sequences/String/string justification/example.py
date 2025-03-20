# Write a program right align string in given width
# without using rjust() method
# input:
# string --> naresh
# width --> 15
# fill char --> *
# output
# *********naresh



str1=input("Enter any String ")
width=int(input("Enter Width of String "))
fill_char=input("Enter Fill Charachter ")

c=len(str1)
if width>c:
    d=width-c
    str2=d*fill_char+str1
    print(str2)
else:
    print(str1)