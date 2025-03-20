# Replacing multiple values using slicing 
# Index alows replacing one value 
# In order replace multiple values we using slicing 
# Syntax: list-name[start:stop:step]=iterable

a=[10,20,30,40,50,60,70,80,90,100] 
print(a)
a[:2]=[1,2]
print(a)
a[::2]="ABCDE"
print(a)
a[-3:]=[10,20,30]
print(a)
a[2:-2]=[1,2,3,4,5,6]
print(a)

print("=================================")

b=[10,20,30,40,50]
print(b)
b[3:8]=[1,2,3,4,5]
print(b)