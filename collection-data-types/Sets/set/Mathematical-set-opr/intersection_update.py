# intersection_update(*others) 
# set &= other & ... 
# Update the set, keeping only elements found in it and al others.


a={1,2,3}
b={1,2,4}
a.intersection_update(b)
print(a)


x={1,2,3}
y={1,2,5}
x&=y
print(x)