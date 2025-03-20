# List inside list is ca led nested list 
# Syntax: 
# variable-name=[[value,value],[value,value,value],[value,value]]


a=[[1,2],[2,3]]
print(a)
print(a[0],a[1],sep="\n")

print(a[0][0],a[0][1],a[1][0],a[1][1])

print(a[0][-1],a[0][-2])

print(a[1][-1],a[1][-2])