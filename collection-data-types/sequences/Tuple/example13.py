# Sort a List of Tuples by Second Item – Python 

# For example, given the list 
# [(1, 3), (4, 1), (2, 2)], 
# the goal is to reorder it by the second item, 
# resulting in [(4, 1), (2, 2), (1, 3)].


a=[(1, 3), (4, 1), (2, 2)] 
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j][-1]>a[j+1][-1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)