# Merging dictionaries without using merge operator (|) 
# This can be done by unpacking items of dictionary using **


d1={1:10,2:20,3:30}
d2={4:40,5:50}
d3={**d1}
print(d3)
d4={**d1,**d2}
print(d4)