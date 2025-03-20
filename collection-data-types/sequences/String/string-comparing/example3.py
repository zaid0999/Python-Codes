# Python program to print even length words in a string 
# input: python is a programming language 
# output: python is language 


str1="python is programming langauge"

a=str1.split()
for s in a:
    if len(s)%2==0:
        print(s,end=' ')
        