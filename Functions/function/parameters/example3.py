# Functions with parameters in python are caled generic functions, these parameters receives values of any type. 

# Example:

def maximum(a,b):
    if a>b:
        return a
    else:
        return b

res1=maximum(66,33)
res2=maximum(8.3,9.2)
res3=maximum("a","A")
print(res1,res2,res3)
