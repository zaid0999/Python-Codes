# d | other 

# Create a new dictionary with the merged keys and values of d and other, which must both be dictionaries. The values of other take priority when d and other share keys. 

# Added in version 3.9.


d1={1:10,2:20,3:30}
d2={4:40,5:50,6:60}

d3=d1 | d2
print(d1,d2,d3,sep="\n")


print("===============================")



dict4={1:10,2:20}
dict5={3:30,4:40,1:99}

dict6=dict4 | dict5
print(dict4,dict5,dict6,sep="\n")