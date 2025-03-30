def sumofvalues(*a):
    s=0
    for value in a:
        s=s+value
    return s

res1=sumofvalues()
print(res1)
res2=sumofvalues(10,3,6,8,93,5,8)
print(res2)