# Python – Uppercase Half String 
# input: python 
# output could be “PYThon” (uppercase first half) or “pytHON”




str1="python"
str2=str1[:len(str1)//2].upper()+str1[len(str1)//2:].lower()
print(str1)
print(str2)