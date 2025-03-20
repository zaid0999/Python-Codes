# fromhex(string)
# This bytes class method returns a bytes object, decoding the given string object. The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored.



a=bytes.fromhex("41")
print(a)

print()


b=bytes.fromhex("ff")
print(b)

for x in b:
    print(x)


print()


c=bytes.fromhex("ff 0f 0a")
print(c)