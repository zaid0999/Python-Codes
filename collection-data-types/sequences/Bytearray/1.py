# Bytearray
# bytearray objects are a mutable counterpart to bytes objects.






a=bytearray()
print(a)


print()



a.append(66)
print(a)

print()

a.extend([66,67,68,69])
print(a)

print()


del a[0]
print(a)

a[0]=98
print(a)

for x in a:
    print(x)