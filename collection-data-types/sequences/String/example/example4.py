# Reverse Words in a Given String in Python 
# input : python programming language 
# output: language programming python 

str1="python programming langauage"

a=str1.split()
a=a[::-1]
str2=" ".join(a)
print(str2)