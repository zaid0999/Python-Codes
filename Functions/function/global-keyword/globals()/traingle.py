# Finding Area of Triangle 

base=0.0 # Global Variable
height=0.0 # Global Variable

def read():
    global base,height
    base=float(input("Base: "))
    height=float(input("Height: "))

def find_area():
    area=0.5*base*height
    print(f'Area of triangel is {area:.2f}')

read()
find_area()