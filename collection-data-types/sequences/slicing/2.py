# Sequence-name[::] (OR) sequence-name[:] 


A=[10,20,30,40,50,60,70,80,90,100]
print(A)

print()

B=A[::]
print(B)

print()

C=A[:]
print(C)

print("=========================================")

# Sequence-name[::step] 

A=list(range(10,110,10))
print(A)

print()

B=A[::1]
print(B)

print()

C=A[::2]
print(C)

print()

D=A[::-1]
print(D)

print()

E=A[::-2]
print(E)


# Example:

# r1=range(10,110,10)
# r2=r1[0]
# print(r2)

# r3=r1[1]
# print(r3)

# r4=r1[-1]
# print(r4)

# r5=r1[-3]
# print(r5)

# r2=r1[::-1]
# r3=r2[0]
# print(r3)

# r3=r1[0:5:1]
# for value in r3:
#     print(value,end=' ')
print("=========================================")


# Sequence-name[start::] 

A=[10,20,30,40,50,60,70,80,90,100]
print(A)

print()


B=A[5::]
print(B)

print()

C=A[-8::]
print(C)

print("=========================================")

# Sequence-name[:stop:] 

A=list(range(10,110,10))

B=A[:5:]
print(B)

print()

C=A[:-5:]
print(C)

print()

D=A[:-3:]
print(D)

print()

E=A[:-8:]
print(E)

print("=========================================")

# Sequence-name[start:stop:] 

A=[10,20,30,40,50,60,70,80,90,100] 

B=A[0:6]
print(B)

print()

C=A[-6:-9]
print(C)

D=A[-9:-6]
print(D)

print("=========================================")

# Sequence-name[start::step] 

A=list(range(10,110,10))

B=A[4::2]
print(B)

C=A[-4::-2]
print(C)

print("=========================================")

# Sequence-name[:stop:step] 

A=list(range(10,110,10))

B=A[:7:1]
print(B)

C=A[:-5:1]
print(C)

D=A[:-5:-1]
print(D)