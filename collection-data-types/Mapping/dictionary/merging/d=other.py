# d |= other 

# Update the dictionary d with keys and values from other, which may be either a mapping or an iterable of key/value pairs. The values of other take priority when d and other share keys.


d1={1:10,2:20,3:30}
d2={4:40,5:50}
d1|=d2
print(d1)