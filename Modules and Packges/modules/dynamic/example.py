# Write a program to find sqrt of input number 

import importlib 

num=int(input("Enter any number: "))
m=input("module name to find sqrt: ")
module=importlib.import_module(m)
res=module.sqrt(num)
print(res)