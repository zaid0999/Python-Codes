# Update Each Element in Tuple List-Python
# For example, 
# given a = [(1, 3, 4), (2, 4, 6), (3, 8, 1)] and 
# ele = 4, the goal is to add 4 to every element in each tuple, 
# resulting in [(5, 7, 8), (6, 8, 10), (7, 12, 5)]. 


a=[(1,3,4),(2,4,6),(3,8,1)]
ele=4
b=[]
for row in a:
    c=[]
for value in row:
    value=value+ele
    c.append(value)
    b.append(tuple(c))
print(a)
print(b)


d=[tuple([value+ele for value in row]) for row in a]
print(d)