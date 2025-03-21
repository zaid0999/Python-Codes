# Python – Find missing and additional values in two lists 

a = [1, 2, 3, 4, 5, 6] 
b = [4, 5, 6, 7, 8] 

c=set(b)-set(a)
d=set(a)-set(b)
print(f'a list {a}')
print(f'b list {b}')
print(f'missing values in a {c}')
print(f'additiional values in a {d}')
e=set(a)-set(b)
f=set(b)-set(a)
print(f'missing values in b {e}')
print(f'additonal values in b {f}')