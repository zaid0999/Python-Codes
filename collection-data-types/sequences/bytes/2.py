# In addition to the literal forms, bytes objects can be created in a number of other ways:

# A zero-filled bytes object of a specified length: bytes(10)
# From an iterable of integers: bytes(range(20))
# Copying existing binary data via the buffer protocol: bytes(obj)



b1=bytes(5)
print(b1)
for value in b1:
    print(value)


print()

# b1[0]=65
# del b1[0]


b2=bytes(range(65,70))
print(b2)


b3=bytes(range(97,102))
print(b3)



print("========================")


b4=bytes([65,66,67,68,69,55])
print(b4)




print("========================")





b6=bytes("ABC",encoding='utf-8')
print(b6)

for x in b6:
    print(x)


print()


b1=b'ABC'
b2=bytes(b1)
print(b1,b2,sep="\n")