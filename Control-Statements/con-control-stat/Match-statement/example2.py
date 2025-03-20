print("***MENU***")
print("1.Area of Triangle")
print("2.Area of Rectangle")
print("3.Exit")
opt=int(input("Enter Your Option "))
match(opt):
    case 1:
        base=float(input("Enter Base "))
        height=float(input("Enter Height "))
        area=0.5*base*height
        print(f'Area of triangle is {area:.2f}')
    case 2:
        length=float(input("Enter Base "))
        breadth=float(input("Enter Breadth "))
        area=length*breadth
        print(f'Area of Rectangle is {area:.2f}')
    case 3:
        print("Thanks using Menu")
    case _:
        print("Input options from 1-3")