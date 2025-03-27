# zip(*iterables)  
# Iterate over several iterables in paralel, producing tuples with an item from each one. 


names=["naresh","ramesh","suresh"]
salaries=[10000,20000,30000]
emp=dict(zip(names,salaries))
print(emp)


print()


dict1=dict(zip(range(1,6),range(10,60,10)))
print(dict1)