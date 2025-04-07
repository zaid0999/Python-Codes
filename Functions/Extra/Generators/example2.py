# Generator Function

def int_itr():
    n=0
    while True:
        yield n
        n=n+1

x=int_itr() # Creating iterator object
for y in x:
    print(y)
    if y>=20:
        break