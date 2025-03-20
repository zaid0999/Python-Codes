a=[10,20]
print(a)

print()

a.extend([30,40,50])
print(a)

print()

a.extend(range(60,110,10))
print(a)

a.extend("ABC")
print(a)

print("==============================")

# difference between append and extend

b=[]
b.append(10)
b.append(20)
print(b)

b.extend([30,40,50])
print(b)

b.append([60,70,80])
print(b)

b.extend("ABC")
print(b)

b.append("ABC")
print(b)

print("==============================================")
# How to append more than one value without using extend method?

C=[10,20,30] 
print(C) 
[10, 20, 30] 
C[len(C):]=[40,50,60,70] 
print(C) 
[10, 20, 30, 40, 50, 60, 70] 
C[len(C):]="ABCD" 
print(C) 
[10, 20, 30, 40, 50, 60, 70, 'A', 'B', 'C', 'D'] 
C[len(C):]=range(1,3) 
print(C) 
[10, 20, 30, 40, 50, 60, 70, 'A', 'B', 'C', 'D', 1, 2]