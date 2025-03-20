# Write a program input three integer nnumbers 
# and maximum

a=int(input("Enter First Number "))
b=int(input("Enter Second Number "))
c=int(input("Enter Third Number "))

if a==b==c:
    print("Equal")
elif a>=b and a>=c:
    print(f'{a} First Is Max')
elif b>=a and b>=c:
    print(f'{b} Second Is Max')
elif c>=a and c>=b:
    print(f'{c} Thirs Is Max')