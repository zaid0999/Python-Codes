# Syntax1: del <list-name>[index] 
# Syntax2: del <list-name>[start:stop:step]

a=[10,20,30,40,50]
print(a)
del a[0]
print(a)

print()

del a[-2]
print(a)

print()

# del a[4]
# print(a)

print("=======================")

b=list(range(10,110,10))
print(b)
del b[0:3]
print(b)

del b[-2]
print(b)

del b[2:-2]
print(b)

del b[::]
print(b)