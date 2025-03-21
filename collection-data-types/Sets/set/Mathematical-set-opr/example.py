# Python – Check if two lists have at-least one element common

a=[1,2,3,4]
b=[5,6,3,8]
c=set(a)&set(b)
if len(c)>0:
    print(f'common element {c}')
else:
    print("no common elements")