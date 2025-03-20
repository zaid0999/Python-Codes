# Python program to check whether the string is Symmetrical or Palindrome


str1=input("Enter Any String ")
if len(str1)%2==0:
    m=len(str1)//2
    h1=str1[:m]
    h2=str1[m:]
    if h1==h2:
        print("String is Symmetrical")
    else:
        print("Strin is not Symmetrical")
else:
    print("String is not Symmetrical")

str2=str1[::-1]
if str1==str2:
    print("String is Palindrome")
else:
    print("String is not Palindrome")