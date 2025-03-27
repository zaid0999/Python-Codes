# fromkeys(iterable, value=None, /) 
# Create a new dictionary with keys from iterable and values set to value.

# dict.fromkeys(iterable,value=None)

d1=dict.fromkeys(range(1,10))
print(d1)

d2=dict.fromkeys(range(1,6),0)
print(d2)

print()

d3=dict.fromkeys("ABCDE")
print(d3)