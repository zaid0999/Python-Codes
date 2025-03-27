# How map more than one value to a single key? 

# n dictionary key is mapped with one or more than one value More than one value is grouped inside colection (List, Tuple, Dictionary, Set, Frozenset,…) 


d1={1:[10,20,30],
    2:[40,50,60],
    3:[70,80,90]}
print(d1)

print(d1[1])

print(d1[2])

print(d1[3])


print("================================")


print(d1[1][0])
print(d1[1][1])
print(d1[1][2])

print()


print(d1[2][-1])
print(d1[2][2])