# Write a program center alignment of string in given width
# without using center method
# input
# string ==> naresh
# width ==> 10
# fill_char ==> *
# **naresh**



str1=input("Enter Any String ")
width=int(input("Enter Display Width "))
fill_char=input("Enter Fill Charachter ")

l=len(str1)
if l<width:
    diff=width-l
    x=diff//2
    str2=x*fill_char+str1+(diff-x)*fill_char
    print(str2)
else:
    print(str1)